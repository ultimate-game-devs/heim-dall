from time import localtime

from gettingHumid import gethumid
from gettingTemp import gettemp
from setUpSensor import setupdht11

while True:
	now = localtime()
	print(f'~~~ {now.tm_hour}:{now.tm_min}:{now.tm_sec} ~~~')
	sensor = setupdht11()
	temperature = gettemp(sensor)
	humidity = gethumid(sensor)
	if humidity is not None and temperature is not None:
		print(f'Temperature - {temperature}°C | Humidity - {humidity}%')
	else:
		raise 'Error: Temperature or Huminity None'
