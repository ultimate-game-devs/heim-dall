import adafruit_dht
import board


def setupdht11() -> adafruit_dht.DHT11:
	return adafruit_dht.DHT11(board.D4)
