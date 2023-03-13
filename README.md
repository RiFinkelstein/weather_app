# weather_app
###This Python script retrieves weather information for a given location using the OpenWeatherMap API. The script asks the user for the location and the unit of temperature they want to receive weather information on.

##Requirements
Python 3.x
requests library
argparse library
tabulate library
pytz library
Usage
The script takes two optional command-line arguments:

--location: The location for which to get weather information. If this argument is not provided, the script will prompt the user to enter one or more locations.
--unit: The temperature unit to display (C or F). If this argument is not provided, the script will prompt the user to enter the temperature unit.
To run the script, open a terminal or command prompt and navigate to the directory containing the script. Then, run the following command:
python weather_info.py --location <LOCATION> --unit <UNIT>
Replace <LOCATION> with the location for which to get weather information, and <UNIT> with the temperature unit to display (C or F).

##Output
The script will display the following information for each location entered:

The date and time right now
The temperature in the specified unit
The humidity
The wind speed
The weather description
The script will also handle errors if the location is not found or if there is an error with the API request.

##API Key
The script uses the OpenWeatherMap API to retrieve weather information. To use the script, you will need to obtain an API key from the OpenWeatherMap website and replace the api_key variable in the script with your own API key.
