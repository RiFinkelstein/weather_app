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
