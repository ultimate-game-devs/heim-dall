import adafruit_dht


def gethumid(sensor: adafruit_dht.DHT11) -> float | None:
	try:
		humidity = sensor.humidity
		sensor.exit()
		return humidity
	except Exception as error:
		print(error)
		return None
