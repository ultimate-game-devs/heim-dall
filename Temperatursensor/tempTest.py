import adafruit_dht
import board
import time

DHT_SENSOR = Adafruit_DHT.DHT11(board.D4)

while True:
    try:
        print(time.time())
        temperature = DHT_SENSOR.temperature
        humidity = DHT_SENSOR.humidity
        if humidity is not None and temperature is not None:
            print(f"Temperature - {temperature}°C | Humidity - {humidity}%")
        else:
            print(f"Error: Temperature ({temperature}) or Huminity ({humidity}) None")
    except Exception as error:
        DHT_SENSOR.exit()
        raise error
    time.sleep(3)
