from gpiozero import DHT11
from time import sleep

sensor = DHT11(4)  # GPIO4

while True:
    temperature = sensor.temperature
    humidity = sensor.humidity
    if temperature is not None and humidity is not None:
        print(f"Temp: {temperature}°C, Humidity: {humidity}%")
    else:
        print("Failed to get reading. Trying again...")
    sleep(2)


