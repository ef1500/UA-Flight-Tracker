# United Airlines Flight Tracker
CLI Tool for obtaining flight information about a United Airlines Flight Number

## Usage
```
usage: uflight.py [-h] [-f FLIGHT] [-d DATE] [-e EXPORT]

CLI Tool to Track United Flights

optional arguments:
  -h, --help            show this help message and exit
  -f FLIGHT, --flight FLIGHT
                        Flight Number
  -d DATE, --date DATE  Flight Data (YYYY-MM-DD)
  -e EXPORT, --export EXPORT
                        Exported the formatted data to a file
```
### Basic Usage
##### Track a flight

`python3 uflight.py -f 380` (The date argument automatically defaults to today)

##### Track a flight by date

`python3 uflight.py -f 380 -d 2022-02-01`

##### Track a flight and export the data

`python3 uflight.py -f 380 -e flightdata.txt`

### Example Use
```
> python3 uflight.py -f 2275

UNITED FLIGHT 2275
    AIRCRAFT INFORMATION:
        Cabin Count: 2
        Aircraft ID: 7533
        Aircraft Code: 739
        Aircraft Name (Short): B737-900
        Aircraft Name (Long): Boeing 737 MAX 9
        Wifi Avaliable: True

    FLIGHT INFORMATION:
        Flight Number: 2275

        Status: Arrived at gate
        Status (Short): Landed

        Scheduled Departure Time: 8/4/2022 7:20 AM
        Scheduled Arrival Time: 8/4/2022 9:57 AM
        Scheduled Departure Time (GMT): 2022-08-04T12:20:00
        Scheduled Arrival Time (GMT): 2022-08-04T16:57:00
        Estimated Departure Time: 8/4/2022 7:20 AM
        Estimated Arrival Time: 8/4/2022 9:59 AM
        Actual Departure Time: 8/4/2022 7:19 AM
        Actual Arrival Time: 8/4/2022 10:01 AM

        Departure Terminal: Terminal 1, Concourse C
        Departure Gate: C17
        Arrival Terminal: Main Terminal, Concourse A
        Arrival Gate: A8

        Tracking URL: https://flightaware.com/commercial/custom/united/united_track.rvt?flight=UAL2275&origin=KORD&destination=KSEA&date=20220804&time=1220&hash=3222331026dde25e863d03173ea876534604fed9aa7b42cb49da2fdf4ffdf255
```
