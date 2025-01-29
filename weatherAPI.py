#First try
import requests
import os
from dotenv import load_dotenv
from Geolocation import GeolocationResult, Location

load_dotenv()

api_key = os.getenv('API_KEY')

#Geolocation
result = requests.post(f"https://www.googleapis.com/geolocation/v1/geolocate?key={api_key}").json()
location = Location(result["location"]["lat"], result["location"]["lng"])
geolocation = GeolocationResult(result["accuracy"], location)