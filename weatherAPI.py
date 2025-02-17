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
	CurrentWeatherResponse,
	ForecastList,
	City,
	ForecastWeatherResponse,
)

load_dotenv()

google_key = os.getenv('GOOGLE_KEY')
weather_key = os.getenv('WEATHER_KEY')

# Geolocation
google_result = requests.post(
	f'https://www.googleapis.com/geolocation/v1/geolocate?key={google_key}',
).json()
# print(google_result)

location = Location(google_result['location']['lat'], google_result['location']['lng'])
geolocation = GeolocationResult(google_result['accuracy'], location)

# Current Weather API

curr_result = requests.post(
	f'https://api.openweathermap.org/data/2.5/weather?lat={geolocation.location.lat}&lon={geolocation.location.lng}&appid={weather_key}&units=metric&lang=de'
).json()
# print(curr_result)

curr_coord = Coord(curr_result['coord']['lon'], curr_result['coord']['lat'])
curr_weather = []
for i in range(len(curr_result['weather'])):
	curr_weather.append(
		Weather(
			curr_result['weather'][i]['id'],
			curr_result['weather'][i]['main'],
			curr_result['weather'][i]['description'],
			curr_result['weather'][i]['icon'],
		)
	)
curr_main = Main(
	curr_result['main']['temp'],
	curr_result['main']['feels_like'],
	curr_result['main']['temp_min'],
	curr_result['main']['temp_max'],
	curr_result['main']['pressure'],
	curr_result['main']['humidity'],
	curr_result['main']['sea_level'],
	curr_result['main']['grnd_level'],
)

if 'gust' in curr_result['wind']:
	curr_wind = Wind(
		curr_result['wind']['speed'],
		curr_result['wind']['deg'],
		curr_result['wind']['gust'],
	)
else:
	curr_wind = Wind(curr_result['wind']['speed'], curr_result['wind']['deg'])

curr_spezial_weather = None
if 'rain' in curr_result:
	curr_spezial_weather = Rain(curr_result['rain']['1h'])
elif 'snow' in curr_result:
	curr_spezial_weather = Snow(curr_result['snow']['1h'])

curr_clouds = Clouds(curr_result['clouds']['all'])
curr_sys = Sys(
	curr_result['sys']['type'],
	curr_result['sys']['id'],
	curr_result['sys']['country'],
	curr_result['sys']['sunrise'],
	curr_result['sys']['sunset'],
)
curr_weather_response = CurrentWeatherResponse(
	coord=curr_coord,
	weather=curr_weather,
	base=curr_result['base'],
	main=curr_main,
	visibility=curr_result['visibility'],
	wind=curr_wind,
	spezial_weather=curr_spezial_weather,
	clouds=curr_clouds,
	dt=curr_result['dt'],
	sys=curr_sys,
	timezone=curr_result['timezone'],
	city_id=curr_result['id'],
	name=curr_result['name'],
	cod=curr_result['cod'],
)

fc_result = requests.post(
	f'https://api.openweathermap.org/data/2.5/forecast?lat={geolocation.location.lat}&lon={geolocation.location.lng}&appid={weather_key}&units=metric&lang=de'
).json()

fc_list = []
for j in range(len(fc_result['list'])):
	fc_main = Main(
		fc_result['list'][j]['main']['temp'],
		fc_result['list'][j]['main']['feels_like'],
		fc_result['list'][j]['main']['temp_min'],
		fc_result['list'][j]['main']['temp_max'],
		fc_result['list'][j]['main']['pressure'],
		fc_result['list'][j]['main']['humidity'],
		fc_result['list'][j]['main']['sea_level'],
		fc_result['list'][j]['main']['grnd_level'],
	)

	fc_weather = []
	for i in range(len(fc_result['list'][j]['weather'])):
		fc_weather.append(
			Weather(
				fc_result['list'][j]['weather'][i]['id'],
				fc_result['list'][j]['weather'][i]['main'],
				fc_result['list'][j]['weather'][i]['description'],
				fc_result['list'][j]['weather'][i]['icon'],
			)
		)

	fc_clouds = Clouds(fc_result['list'][j]['clouds']['all'])

	if 'gust' in fc_result['list'][j]['wind']:
		fc_wind = Wind(
			fc_result['list'][j]['wind']['speed'],
			fc_result['list'][j]['wind']['deg'],
			fc_result['list'][j]['wind']['gust'],
		)
	else:
		fc_wind = Wind(
			fc_result['list'][j]['wind']['speed'], fc_result['list'][j]['wind']['deg']
		)

	fc_spezial_weather = None
	if 'rain' in fc_result['list'][j]:
		fc_spezial_weather = Rain(fc_result['list'][j]['rain']['1h'])
	elif 'snow' in fc_result['list'][j]:
		fc_spezial_weather = Snow(fc_result['list'][j]['snow']['1h'])

	fc_list.append(
		ForecastList(
			fc_result['list'][j]['dt'],
			fc_main,
			fc_weather,
			fc_clouds,
			fc_wind,
			fc_result['list'][j]['visibility'],
			fc_result['list'][j]['pop'],
			fc_result['list'][j]['sys'],
			fc_result['list'][j]['dt_txt'],
			fc_spezial_weather,
		)
	)

fc_coord = Coord(fc_result['city']['coord']['lon'], fc_result['city']['coord']['lat'])

fc_city = City(
	fc_result['city']['id'],
	fc_result['city']['name'],
	fc_coord,
	fc_result['city']['country'],
	fc_result['city']['population'],
	fc_result['city']['timezone'],
	fc_result['city']['sunrise'],
	fc_result['city']['sunset'],
)

fc_response = ForecastWeatherResponse(
	fc_result['cod'], fc_result['message'], fc_result['cnt'], fc_list, fc_city
)

fc_response.print_forecast()
