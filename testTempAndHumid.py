from time import localtime, sleep

from gettingTemp import getTemp
from gettingHumid import getHumid
from setUpSensor import setUpDHT11ONFour

while True:
    now = localtime()
    print(f"~~~ {now.tm_hour}:{now.tm_min}:{now.tm_sec} ~~~")
    sensor = setUpDHT11ONFour()
    temperature = getTemp(sensor)
    humidity = getHumid(sensor)
    if humidity is not None and temperature is not None:
        print(f"Temperature - {temperature}°C | Humidity - {humidity}%")
    else:
        raise "Error: Temperature or Huminity None"
