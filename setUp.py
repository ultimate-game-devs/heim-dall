import adafruit_dht
import board


def dht11(pin_number: int) -> adafruit_dht.DHT11:
	board_pin = getattr(board, f'D{pin_number}')
	return adafruit_dht.DHT11(board_pin)
