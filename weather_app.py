import requests
import argparse
from tabulate import tabulate
import datetime
import pytz


parser = argparse.ArgumentParser(
    description='Get weather information for a location')
parser.add_argument('--location', type=str, required=False,
                    help='The location for which to get weather information')
parser.add_argument('--unit', type=str, required=False,
                    help='The temperature unit to display (C or F)')

args = parser.parse_args()
location = args.location

if args.location:
    location = args.location
else:
    location = input(
        "Enter the location for which to get weather information: ")

print(location)

# ask what tempurture unit
if args.unit:
    unit = args.unit.upper()
else:
    unit = input("Enter the temperature unit to display (C or F): ").upper()


api_key = "c80b1a2d82ff9185cbe2051652745fb7"

# Make the API request
url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Define datetime_str
datetime_str = ""

# Define temperature
temperature = 0

# Check if "main" key exists in data dictionary
if "main" in data:
    # Extract the relevant weather information
    temperature_kelvin = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"]
    timezone_offset = data["timezone"]

    # Convert temperature to the specified unit
    if unit == "F":
        temperature = (temperature_kelvin) * 9/5 + 32
        unit_symbol = "°F"
    elif unit == "C":
        temperature = temperature_kelvin - 273.15
        unit_symbol = "°C"
    else:
        temperature = temperature_kelvin
        unit_symbol = "K"

    # Get the timezone for the location
    timezone = pytz.timezone(f'Etc/GMT{timezone_offset//3600:+d}')

    # Get the current time in the timezone of the location
    now = datetime.datetime.now(tz=timezone)

    # Format the date and time string
    datetime_str = now.strftime("%Y-%m-%d %H:%M:%S %Z%z")

    # Print the weather information
    print(f"The date & time right now is: {datetime_str}")
    print(f"The temperature in {location} is {temperature:.1f} °C")
    print(f"The humidity in {location} is {humidity}%")
    print(f"The wind speed in {location} is {wind_speed} m/s")
    print(f"The weather description in {location} is {description}")

else:
    print("sorry there is an error")
