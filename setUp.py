import adafruit_dht
import board
import digitalio


def dht11(pin_number: int) -> adafruit_dht.DHT11:
	board_pin = getattr(board, f'D{pin_number}')
	return adafruit_dht.DHT11(board_pin)


def motion(pin_number: int) -> digitalio.DigitalInOut:
	board_pin = getattr(board, f'D{pin_number}')
	pir = digitalio.DigitalInOut(board_pin)
	pir.direction = digitalio.Direction.INPUT
	return pir
