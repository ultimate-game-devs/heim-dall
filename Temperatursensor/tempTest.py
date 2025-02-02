import adafruit_dht
import board
import time

dht_sensor = adafruit_dht.DHT11(board.D4)

while True:
    try:
        now = time.localtime()
        print(f"{now.tm_hour}:{now.tm_min}:{now.tm_sec}")
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity
        if humidity is not None and temperature is not None:
            print(f"Temperature - {temperature}°C | Humidity - {humidity}%")
        else:
            print(f"Error: Temperature ({temperature}) or Huminity ({humidity}) None")
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dht_sensor.exit()
        raise error
    time.sleep(3)
