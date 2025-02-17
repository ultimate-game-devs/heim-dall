from typing import List, Literal


class Coord:
	def __init__(self, lon: float, lat: float) -> None:
		self.lon = lon
		self.lat = lat

	@classmethod
	def from_dict(cls, data: dict):
		return cls(data['lon'], data['lat'])


class Weather:
	def __init__(self, weather_id: int, main: str, description: str, icon: str) -> None:
		self.weather_id = weather_id
		self.main = main
		self.description = description
		self.icon = icon

	@classmethod
	def from_dict(cls, data: dict):
		return cls(
			data['id'],
			data['main'],
			data['description'],
			data['icon'],
		)


class Main:
	def __init__(
		self,
		temp: float,
		feels_like: float,
		temp_min: float,
		temp_max: float,
		pressure: int,
		humidity: int,
		sea_level: int,
		grnd_level: int,
	) -> None:
		self.temp = temp
		self.feels_like = feels_like
		self.temp_min = temp_min
		self.temp_max = temp_max
		self.pressure = pressure
		self.humidity = humidity
		self.sea_level = sea_level
		self.grnd_level = grnd_level

	@classmethod
	def from_dict(cls, data: dict):
		return cls(
			data['temp'],
			data['feels_like'],
			data['temp_min'],
			data['temp_max'],
			data['pressure'],
			data['humidity'],
			data['sea_level'],
			data['grnd_level'],
		)


class Wind:
	def __init__(self, speed: float, deg: int, gust: float | None = None) -> None:
		self.speed = speed
		self.deg = deg
		self.gust = gust

	@classmethod
	def from_dict(cls, data: dict):
		if 'gust' in data:
			return cls(
				data['speed'],
				data['deg'],
				data['gust'],
			)
		else:
			return cls(data['speed'], data['deg'])


class Rain:
	def __init__(self, one_h: float) -> None:
		self.one_h = one_h

	@classmethod
	def from_dict(cls, data: dict):
		return cls(data['1h'])


class Snow:
	def __init__(self, one_h: float) -> None:
		self.one_h = one_h

	@classmethod
	def from_dict(cls, data: dict):
		return cls(data['1h'])


class Clouds:
	def __init__(self, cloudiness: int) -> None:
		self.cloudiness = cloudiness

	@classmethod
	def from_dict(cls, data: dict):
		return cls(data['all'])


class Sys:
	def __init__(
		self, sys_type: int, sys_id: int, country: str, sunrise: int, sunset: int
	) -> None:
		self.sys_type = sys_type
		self.sys_id = sys_id
		self.country = country
		self.sunrise = sunrise
		self.sunset = sunset


class CurrentWeatherResponse:
	def __init__(
		self,
		coord: Coord,
		weather: List[Weather],
		base: str,
		main: Main,
		visibility: int,
		wind: Wind,
		clouds: Clouds,
		dt: int,
		sys: Sys,
		timezone: int,
		city_id: int,
		name: str,
		cod: int,
		spezial_weather: Rain | Snow | None = None,
	) -> None:
		self.coord = coord
		self.weather = weather
		self.base = base
		self.main = main
		self.visibility = visibility
		self.wind = wind
		self.spezialWeather = spezial_weather
		self.clouds = clouds
		self.dt = dt
		self.sys = sys
		self.timezone = timezone
		self.city_id = city_id
		self.name = name
		self.cod = cod


class ForecastList:
	def __init__(
		self,
		dt: int,
		main: Main,
		weather: List[Weather],
		clouds: Clouds,
		wind: Wind,
		visibility: int,
		pop: float,
		sys: Literal['n', 'd'],
		dt_txt: str,
		spezial_weather: Rain | Snow | None = None,
	) -> None:
		self.dt = dt
		self.main = main
		self.weather = weather
		self.clouds = clouds
		self.wind = wind
		self.visibility = visibility
		self.pop = pop
		self.spezial_weather = spezial_weather
		self.sys = sys
		self.dt_text = dt_txt

	@classmethod
	def from_dict(cls, data: dict):
		weather = []
		for i in range(len(data['weather'])):
			weather.append(Weather.from_dict(data['weather'][i]))

		spezial_weather = None
		if 'rain' in data:
			spezial_weather = Rain.from_dict(data['rain'])
		elif 'snow' in data:
			spezial_weather = Snow.from_dict(data['snow'])

		return cls(
			data['dt'],
			Main.from_dict(data['main']),
			weather,
			Clouds.from_dict(data['clouds']),
			Wind.from_dict(data['wind']),
			data['visibility'],
			data['pop'],
			data['sys'],
			data['dt_txt'],
			spezial_weather,
		)


class City:
	def __init__(
		self,
		city_id: int,
		name: str,
		coord: Coord,
		country: str,
		population: int,
		timezone: int,
		sunrise: int,
		sunset: int,
	) -> None:
		self.city_id = city_id
		self.name = name
		self.coord = coord
		self.country = country
		self.population = population
		self.timezone = timezone
		self.sunrise = sunrise
		self.sunset = sunset

	@classmethod
	def from_dict(cls, data: dict):
		return cls(
			data['id'],
			data['name'],
			Coord.from_dict(data['coord']),
			data['country'],
			data['population'],
			data['timezone'],
			data['sunrise'],
			data['sunset'],
		)


class ForecastWeatherResponse:
	def __init__(self, fc_result) -> None:
		self.cod = fc_result['cod']
		self.message = fc_result['message']
		self.cnt = fc_result['cnt']
		self.forecast_list = []
		for i in range(len(fc_result['list'])):
			self.forecast_list.append(ForecastList.from_dict(fc_result['list'][i]))
		self.city = City.from_dict(fc_result['city'])

	def print_forecast(self) -> None:
		print(
			f"""
cod: {self.cod}	
message: {self.message}
cnt: {self.cnt}
forecastList: [
	dt: {self.forecast_list[0].dt}
	main: [
		temp: {self.forecast_list[0].main.temp}
		feels_like: {self.forecast_list[0].main.feels_like}
		temp_min: {self.forecast_list[0].main.temp_min}
		temp_max: {self.forecast_list[0].main.temp_max}
		pressure: {self.forecast_list[0].main.pressure}
		humidity: {self.forecast_list[0].main.humidity}
		sea_level: {self.forecast_list[0].main.sea_level}
		grnd_level: {self.forecast_list[0].main.grnd_level}
	]
	weather: [
		id: {self.forecast_list[0].weather[0].weather_id}
		main: {self.forecast_list[0].weather[0].main}
		description: {self.forecast_list[0].weather[0].description}
		icon: {self.forecast_list[0].weather[0].icon}
	]
	cloud: [
		all: {self.forecast_list[0].clouds.cloudiness}
	]
	wind: [
		speed: {self.forecast_list[0].wind.speed}
		deg: {self.forecast_list[0].wind.deg}
		gust: {self.forecast_list[0].wind.gust}
	]
	visibility: {self.forecast_list[0].visibility}
	pop: {self.forecast_list[0].pop}
	rain / snow: {
				f'''[
		1h: {self.forecast_list[0].spezial_weather.one_h}
	]'''
				if self.forecast_list[0].spezial_weather is not None
				else 'None'
			}
]
sys: {self.forecast_list[0].sys}
dt_text: {self.forecast_list[0].dt_text}
city: [
	id: {self.city.city_id}
	name: {self.city.name}
	coord: [
		lon: {self.city.coord.lon}
		lat: {self.city.coord.lat}
	]
	country: {self.city.country}
	population: {self.city.population}
	timezone: {self.city.timezone}
	sunrise: {self.city.sunrise}
	sunset: {self.city.sunset}
]
			"""
		)
