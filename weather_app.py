# Import necessary libraries
import requests
import argparse
from tabulate import tabulate

# Define command line arguments
parser = argparse.ArgumentParser(description='Get weather information for a location')
parser.add_argument('--location', type=str, required=True, help='The location for which to get weather information')

# Parse command line arguments
args = parser.parse_args()
location = args.location


api_key = "c80b1a2d82ff9185cbe2051652745fb7"
# Replace LOCATION with the name of the location you want weather data for
location = "11598"

# Make the API request
url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Extract the relevant weather information
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
description = data["weather"][0]["description"]

# Print the weather information
print(f"The temperature in {location} is {temperature} K")
print(f"The humidity in {location} is {humidity}%")
