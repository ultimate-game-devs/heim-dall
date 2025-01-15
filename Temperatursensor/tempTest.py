import adafruit_dht
from gpiozero import Device
from gpiozero.pins.native import NativeFactory

Device.pin_factory = NativeFactory()

dht_sensor = adafruit_dht.DHT11(4)

try:
    temperature = dht_sensor.temperature
    humidity = dht_sensor.humidity
    print(f"Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%")
except RuntimeError as e:
    print(f"Error reading sensor: {e}")

