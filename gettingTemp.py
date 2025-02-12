import adafruit_dht


def gettemp(sensor: adafruit_dht.DHT11) -> float | None:
	try:
		temperature = sensor.temperature
		sensor.exit()
		return temperature
	except Exception as error:
		print(error)
		return None
