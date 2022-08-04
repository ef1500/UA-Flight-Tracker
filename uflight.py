# uflight.py
# ef1500
import argparse
import datetime
from united_tracker import *


today = datetime.date.today().__str__()

argparser = argparse.ArgumentParser(description="CLI Tool to Track United Flights")
argparser.add_argument('-f', '--flight', type=str, help="Flight Number")
argparser.add_argument('-d', '--date', type=str, default=today, help="Flight Data (YYYY-MM-DD)")
argparser.add_argument('-e', '--export', type=str, required=False, help="Exported the formatted data to a file")

args = argparser.parse_args()
if not args.export:
    UnitedFlight(args.flight, args.date).printFlightData()
if args.export:
    Flight = UnitedFlight(args.flight, args.date)
    Flight.printFlightData()
    Flight.exportFormattedData(args.export)