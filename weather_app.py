"""
This script retrieves weather information for a given location using the OpenWeatherMap API.
Script asks user for location and unit of temperature they want to receive weather info on.
Author: [Rivka Finkelstein]
Date: [03/10/2023]
"""

# Import necessary libraries
import requests
import argparse
from tabulate import tabulate
import datetime
import pytz
import os


# Define command line arguments
parser = argparse.ArgumentParser(
    description='Get weather information for a location')
parser.add_argument('--location', type=str, nargs='+', required=False,
                    help='The location for which to get weather information')
parser.add_argument('--unit', type=str, required=False,
                    help='The temperature unit to display (C or F)')

# Parse the command line arguments
args = parser.parse_args()

# Get the location from command line arguments or user input
if args.location:
    user_locations = args.location
else:
    user_locations = []
    while True:
        user_location = input(
            'Enter the location for which to get weather information: ')
        if not user_location:
            break
        user_locations.append(user_location)


# Get the temperature unit from command line arguments or user input
if args.unit:
    unit = args.unit.upper()
else:
    while True:
        unit = input(
            'Enter the temperature unit to display (C or F): ').upper()
        if unit in ['C', 'F']:
            break
        else:
            print('Invalid temperature unit! please enter \'C\' or \'F\'.')

# Set the API key for the OpenWeatherMap API
api_key = 'c80b1a2d82ff9185cbe2051652745fb7'

# Build the API request URL
# url = f'http://api.openweathermap.org/data/2.5/weather?q={user_location}&appid={api_key}'\

# Initialize list to store weather information for each location
weather_info = []

# Loop over all locations and retrieve weather information
for user_location in user_locations:
    # Build the API request URL
    url = f'http://api.openweathermap.org/data/2.5/weather?q={user_location}&appid={api_key}'
    # Send the API request and get the response
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as error:
        print(
            f'Sorry, there was an error getting weather information for {user_location}.')
        print(f'Error message: {error}')
        continue
    except requests.exceptions.ConnectionError as error:
        print(f'Sorry, could not establish connection to weather API.')
        print(f'Error message: {error}')
        continue
    except requests.exceptions.Timeout as error:
        print(f'Sorry, connection to weather API timed out.')
        print(f'Error message: {error}')
        continue
    except requests.exceptions.RequestException as error:
        print(f'Sorry, there was an error with the request to weather API.')
        print(f'Error message: {error}')
        continue

    # Check if the API returned a 404 error (location not found)
    if response.status_code == 404:
        print(
            f'Sorry, {user_location} not found!.')
        print(f'Error code: {response.status_code}')
        continue

    # Check if the API request was successful
    if response.status_code != 200:
        print(
            f'Sorry, there was an error getting weather information for {user_location}.')
        print(f'Error code: {response.status_code}')
        continue

    # Parse the JSON response
    data = response.json()

    # Check if "main" key exists in data dictionary
    if 'main' not in data:
        print(
            f'Sorry, there was an error getting weather information for {user_location}.')
        exit()

    # Extract the relevant weather information
    temperature_kelvin = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    description = data['weather'][0]['description']
    timezone_offset = data['timezone']

    # Convert temperature to the specified unit
    if unit == 'F':
        temperature = (temperature_kelvin) * 9/5 + 32
        unit_symbol = '°F'
    else:
        temperature = temperature_kelvin - 273.15
        unit_symbol = '°C'

    # Get the timezone for the location
    timezone = datetime.timedelta(seconds=timezone_offset)

    # Get the current time in the timezone of the location
    now = datetime.datetime.utcnow().replace(tzinfo=pytz.utc) + timezone

    # Format the date and time string
    datetime_str = now.strftime('%Y-%m-%d %H:%M:%S %Z%z')

    # Print the weather information
    print(f'The date & time right now is: {datetime_str}')
    print(f'The temperature in {user_location} is {temperature:.1f} °C')
    print(f'The humidity in {user_location} is {humidity}%')
    print(f'The wind speed in {user_location} is {wind_speed} m/s')
    print(f'The weather description in {user_location} is {description}')
