from time import localtime, sleep

from gettingTemp import getTemp
from gettingHumid import getHumid

while True:
    now = localtime()
    print(f"~~~ {now.tm_hour}:{now.tm_min}:{now.tm_sec} ~~~")
    print(f"Temperatur {getTemp()} | Humidity {getHumid()}")
