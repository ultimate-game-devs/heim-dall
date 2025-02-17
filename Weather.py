from typing import List

class Coord:
    def __init__(
            self, 
            lon:float, 
            lat:float
        ) -> None:
        self.lon = lon
        self.lat = lat

class Weather:
    def __init__(
            self, 
            weather_id:int, 
            main:str, 
            description:str, 
            icon:str
        ) -> None:
          self.weather_id = weather_id
          self.main = main
          self.description = description
          self.icon = icon

class Main:
    def __init__(
            self, 
            temp:float, 
            feels_like:float, 
            temp_min:float, 
            temp_max:float, 
            pressure:int, 
            humidity:int, 
            sea_level:int, 
            grnd_level:int
        ) -> None:
        self.temp = temp
        self.feels_like = feels_like
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.pressure = pressure
        self.humidity = humidity
        self.sea_level = sea_level
        self.grnd_level = grnd_level

class Wind:
    def __init__(
            self, 
            speed:float, 
            deg:int, 
            gust:float
        ) -> None:
        self.speed = speed
        self.deg = deg
        self.gust = gust

class Rain:
    def __init__(
            self, 
            one_h:float
        ) -> None:
        self.one_h = one_h

class Snow:
    def __init__(
            self, 
            one_h:float
        ) -> None:
        self.one_h = one_h

class Clouds:
    # all = cloudiness, but all is a reserved keyword.
    def __init__(
            self, 
            cloudiness:int
        ) -> None:
        self.cloudiness = cloudiness

class Sys:
    def __init__(
            self, 
            sys_type:int, 
            sys_id:int, 
            country:str, 
            sunrise:int, 
            sunset:int
        ) -> None:
        self.sys_type = sys_type
        self.sys_id = sys_id
        self.country = country
        self.sunrise = sunrise
        self.sunset = sunset

class CurrentWeatherRespond:
    def __init__(
            self, 
            coord:Coord, 
            weather:List[Weather], 
            base:str, main:Main, 
            visibility:int, 
            wind:Wind, 
            rain:Rain, 
            snow:Snow, 
            clouds:Clouds,
            dt: int, 
            sys:Sys, 
            timezone:int, 
            city_id:int, 
            name:str, 
            cod:int
        ) -> None:
        self.coord = coord
        self.weather = weather 
        self.base = base
        self.main = main
        self.visibility = visibility
        self.wind = wind
        self.rain = rain
        self.snow = snow
        self.clouds = clouds
        self.dt = dt
        self.sys = sys
        self.timezone = timezone
        self.city_id = city_id
        self.name = name
        self.cod = cod
