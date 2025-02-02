import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

while True:
    print(time.time())
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(f"Temperature - {temperature} | Humidity - {humidity}")
    else:
        print(f"Error: Temperature ({temperature}) or Huminity ({humidity}) None")
    time.sleep(3)
