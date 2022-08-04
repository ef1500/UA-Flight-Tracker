# United Flight Tracker
# EF1500
import requests
from dataclasses import dataclass

@dataclass
class GenericFlight:
    carrierCode: str
    flightnumber: str
    flightDate: str
    
@dataclass
class GenericShip:
    cabinCount: int
    shipId: int
    # Aircraft Codes
    code: str
    shortName: str
    longName: str
    
@dataclass
class operatingCarrier:
    code: str
    name: str
    flightnumber: str
    
@dataclass
class baggage:
    bagTerminal: str
    bagClaimUnit: str
    
class UnitedFlight:
    
    API_ENDPOINT = "https://mobileapi.united.com/flightstatusservice/api/getflightstatus_uaandstar"
    
    headers = {
        'Content-Type' : 'application/json',
        'Accept-Encoding' : 'gzip, deflate',
        'Accept': '*/*',
        'Accept-Language' : 'en-US,en;q=0.9',
        'User-Agent': 'UnitedCustomerFacingIPhone/4.1.58.0 CFNetwork/1325.0.1 Darwin/21.1.0'
    }
    
    @staticmethod
    def ReturnJSONPayload(flightNumber, flightdate):
        # Return a usable JSON Payload for the body
        jsonPayload = {
            "flightDate": flightdate,
            "deviceId": "1",
            "origin": "",
            "languageCode": "en-US",
            "carrierCode": "UA",
            "accessCode": "ACCESSCODE",
            "flightNumber": f"{flightNumber}",
            "application": {
                "id": 1,
                "name": "iOS",
                "version": {
                "minor": "4.1.58",
                "major": "4.1.58",
                "displayText": "",
                "build": ""
                }
            },
            "transactionId": "87673768-D6F5-4253-AF65-F5124BBEA53B|4FB92F9C-1CCC-4AF7-850C-2BD0514EE019"}
        
        return jsonPayload.__str__()
    
    @staticmethod
    def getFlightData(payload):
        # Get the Flight Data
        flightdata = requests.post(UnitedFlight.API_ENDPOINT, data=payload, headers=UnitedFlight.headers)
        if flightdata.status_code != 200:
            print("API Error. Maybe the program no longer works.")
            exit()
        flightdata = flightdata.json()
        return flightdata.get("flightStatusInfo")
    
    def __init__(self, flightNumber, flightDate):
        flightData = UnitedFlight.getFlightData(UnitedFlight.ReturnJSONPayload(flightNumber, flightDate))
        
        try:
            flightBetterData = flightData["segments"][0]
        except:
            print("Invalid Flight Number")
            exit()
        self.Flight = GenericFlight(flightData.get("carrierCode"), flightData.get("flightNumber"), flightData.get("flightDate"))
        
        self.scheduledFlightTime = flightBetterData.get("scheduledFlightTime")
        self.actualFlightTime = flightBetterData.get("actualFlightTime") or "In Flight"
        
        self.estimatedDepartureDateTime = flightBetterData.get("estimatedDepartureDateTime")
        self.estimatedArrivalDateTime = flightBetterData.get("estimatedArrivalDateTime")
        self.actualDepartureDateTime = flightBetterData.get("actualDepartureDateTime")
        self.actualArrivalDateTime  = flightBetterData.get("actualArrivalDateTime")
        self.departureTerminal  = flightBetterData.get("departureTerminal")
        self.arrivalTerminal = flightBetterData.get("arrivalTerminal")
        self.departureGate = flightBetterData.get("departureGate")
        self.arrivalGate = flightBetterData.get("arrivalGate")
        self.status = flightBetterData.get("status")
        self.isWiFiAvailable = flightBetterData.get("isWiFiAvailable")
        self.statusShort = flightBetterData.get("statusShort")
        self.arrivalAirport = flightBetterData.get("arrivalAirport")
        self.departureAirport = flightBetterData.get("departureAirport")
        self.planeMapUrl = flightBetterData.get("planeMapUrl")
        self.scheduledDepartureDateTime = flightBetterData.get("scheduledDepartureDateTime")
        self.scheduledArrivalDateTime = flightBetterData.get("scheduledArrivalDateTime")
        self.scheduledDepartureTimeGMT = flightBetterData.get("scheduledDepartureTimeGMT")
        self.scheduledArrivalTimeGMT = flightBetterData.get("scheduledArrivalTimeGMT")
        self.genericShip = GenericShip(flightBetterData["ship"]["cabinCount"],flightBetterData["ship"]["id"], flightBetterData["ship"]["aircraft"]["code"],flightBetterData["ship"]["aircraft"]["shortName"], flightBetterData["ship"]["aircraft"]["longName"])
        self.operatingcarrier = operatingCarrier(flightBetterData["operatingCarrier"]["code"], flightBetterData["operatingCarrier"]["name"], flightBetterData["operatingCarrier"]["flightNumber"])
        self.flight_baggage = baggage(flightBetterData["baggage"]["bagTerminal"], flightBetterData["baggage"]["bagClaimUnit"])
        
    def printFlightData(self):
        FlightData = f"""
UNITED FLIGHT {self.Flight.flightnumber}
    AIRCRAFT INFORMATION:
        Cabin Count: {self.genericShip.cabinCount}
        Aircraft ID: {self.genericShip.shipId}
        Aircraft Code: {self.genericShip.code}
        Aircraft Name (Short): {self.genericShip.shortName}
        Aircraft Name (Long): {self.genericShip.longName}
        Wifi Avaliable: {self.isWiFiAvailable.__str__()}
        
    FLIGHT INFORMATION:
        Flight Number: {self.Flight.flightnumber}
    
        Status: {self.status}
        Status (Short): {self.statusShort}
        
        Scheduled Departure Time: {self.scheduledDepartureDateTime}
        Scheduled Arrival Time: {self.scheduledArrivalDateTime}
        Scheduled Departure Time (GMT): {self.scheduledDepartureTimeGMT}
        Scheduled Arrival Time (GMT): {self.scheduledArrivalTimeGMT}
        Estimated Departure Time: {self.estimatedDepartureDateTime}
        Estimated Arrival Time: {self.estimatedArrivalDateTime}
        Actual Departure Time: {self.actualDepartureDateTime}
        Actual Arrival Time: {self.actualArrivalDateTime}
        
        Departure Terminal: {self.departureTerminal}
        Departure Gate: {self.departureGate}
        Arrival Terminal: {self.arrivalTerminal}
        Arrival Gate: {self.arrivalGate}
        
        Tracking URL: {self.planeMapUrl}
        """
        print(FlightData)
        
    def exportFormattedData(self, filename):
        FlightData = f"""
UNITED FLIGHT {self.Flight.flightnumber}
    AIRCRAFT INFORMATION:
        Cabin Count: {self.genericShip.cabinCount}
        Aircraft ID: {self.genericShip.shipId}
        Aircraft Code: {self.genericShip.code}
        Aircraft Name (Short): {self.genericShip.shortName}
        Aircraft Name (Long): {self.genericShip.longName}
        Wifi Avaliable: {self.isWiFiAvailable.__str__()}
        
    FLIGHT INFORMATION:
        Flight Number: {self.Flight.flightnumber}
    
        Status: {self.status}
        Status (Short): {self.statusShort}
        
        Scheduled Departure Time: {self.scheduledDepartureDateTime}
        Scheduled Arrival Time: {self.scheduledArrivalDateTime}
        Scheduled Departure Time (GMT): {self.scheduledDepartureTimeGMT}
        Scheduled Arrival Time (GMT): {self.scheduledArrivalTimeGMT}
        Estimated Departure Time: {self.estimatedDepartureDateTime}
        Estimated Arrival Time: {self.estimatedArrivalDateTime}
        Actual Departure Time: {self.actualDepartureDateTime}
        Actual Arrival Time: {self.actualArrivalDateTime}
        
        Departure Terminal: {self.departureTerminal}
        Departure Gate: {self.departureGate}
        Arrival Terminal: {self.arrivalTerminal}
        Arrival Gate: {self.arrivalGate}
        
        Tracking URL: {self.planeMapUrl}
        """
        
        with open(filename, 'w+', encoding='utf-8') as f:
            f.write(FlightData)