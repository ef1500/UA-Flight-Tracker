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