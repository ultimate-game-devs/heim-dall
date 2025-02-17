# First try
import requests
import os
from dotenv import load_dotenv
from Geolocation import GeolocationResult, Location
from Weather import Coord, Weather, Main, Wind, Rain, Snow, Clouds, Sys, CurrentWeatherRespond

load_dotenv()

google_key = os.getenv('GOOGLE_KEY')
weather_key = os.getenv('WEATHER_KEY')

# Geolocation
google_result = requests.post(
	f'https://www.googleapis.com/geolocation/v1/geolocate?key={google_key}',
).json()
location = Location(google_result['location']['lat'], google_result['location']['lng'])
geolocation = GeolocationResult(google_result['accuracy'], location)


weather_result = requests.post(
	f'https://api.openweathermap.org/data/2.5/weather?lat={geolocation.location.lat}&lon={geolocation.location.lng}&appid={weather_key}&units=metric&lang=de'
).json()

coor = Coord(
    weather_result['coord']['lon'], 
    weather_result['coord']['lat']
)

# Print the weather_result to debug the structure
print(weather_result)

# Extract weather information with error handling
try:
    weather = Weather(
        weather_result['weather'][0]['id'],  # Corrected key name
        weather_result['weather'][0]['main'],
        weather_result['weather'][0]['description'],
        weather_result['weather'][0]['icon']
    )
except KeyError as e:
    print(f"KeyError: {e} is missing in the weather data")

main = Main(
	weather_result['main']['temp'],
    weather_result['main']['feels_like'],
    weather_result['main']['temp_min'],
    weather_result['main']['temp_max'],
	weather_result['main']['pressure'],
	weather_result['main']['humidity'],
	weather_result['main']['sea_level'],
	weather_result['main']['grnd_level']
)
wind = Wind(
	weather_result['wind']['speed'],
	weather_result['wind']['deg'],
	weather_result['wind']['gust']
)
rain =Rain(
	weather_result['rain']['1h']
)
snow = Snow(
	weather_result['snow']['1h']
)
clouds = Clouds(
	weather_result['clouds']['cloudiness']
)
sys = Sys(
    weather_result['sys']['sys_type'],
    weather_result['sys']['sys_id'],
    weather_result['sys']['country'],
	weather_result['sys']['sunrise'],
    weather_result['sys']['sunset']    
)
weather_desciption = CurrentWeatherRespond(
	
)


print(weather_result)
