# First try
import os

import requests
from dotenv import load_dotenv

from Geolocation import GeolocationResult, Location
from Weather import (
	Coord,
	Weather,
	Main,
	Wind,
	Rain,
	Snow,
	Clouds,
	Sys,
	CurrentWeatherRespond,
)

load_dotenv()

google_key = os.getenv('GOOGLE_KEY')
weather_key = os.getenv('WEATHER_KEY')

# Geolocation
google_result = requests.post(
	f'https://www.googleapis.com/geolocation/v1/geolocate?key={google_key}',
).json()
print(google_result)

location = Location(google_result['location']['lat'], google_result['location']['lng'])
geolocation = GeolocationResult(google_result['accuracy'], location)

# Current Weather API

weather_result = requests.post(
	f'https://api.openweathermap.org/data/2.5/weather?lat={geolocation.location.lat}&lon={geolocation.location.lng}&appid={weather_key}&units=metric&lang=de'
).json()
print(weather_result)

coord = Coord(weather_result['coord']['lon'], weather_result['coord']['lat'])
weather = []
for i in range(len(weather_result['weather'])):
	weather.append(
		Weather(
			weather_result['weather'][0]['id'],
			weather_result['weather'][0]['main'],
			weather_result['weather'][0]['description'],
			weather_result['weather'][0]['icon'],
		)
	)
main = Main(
	weather_result['main']['temp'],
	weather_result['main']['feels_like'],
	weather_result['main']['temp_min'],
	weather_result['main']['temp_max'],
	weather_result['main']['pressure'],
	weather_result['main']['humidity'],
	weather_result['main']['sea_level'],
	weather_result['main']['grnd_level'],
)

if 'gust' in weather_result['wind']:
	wind = Wind(
		weather_result['wind']['speed'],
		weather_result['wind']['deg'],
		weather_result['wind']['gust'],
	)
else:
	wind = Wind(weather_result['wind']['speed'], weather_result['wind']['deg'])

spezial_weather = None
if 'rain' in weather_result:
	spezial_weather = Rain(weather_result['rain']['1h'])
elif 'snow' in weather_result:
	spezial_weather = Snow(weather_result['snow']['1h'])

clouds = Clouds(weather_result['clouds']['all'])
sys = Sys(
	weather_result['sys']['type'],
	weather_result['sys']['id'],
	weather_result['sys']['country'],
	weather_result['sys']['sunrise'],
	weather_result['sys']['sunset'],
)
weather_response = CurrentWeatherRespond(
	coord=coord,
	weather=weather,
	base=weather_result['base'],
	main=main,
	visibility=weather_result['visibility'],
	wind=wind,
	spezial_weather=spezial_weather,
	clouds=clouds,
	dt=weather_result['dt'],
	sys=sys,
	timezone=weather_result['timezone'],
	city_id=weather_result['id'],
	name=weather_result['name'],
	cod=weather_result['cod'],
)

print(weather_response)
