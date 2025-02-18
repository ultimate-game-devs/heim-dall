import adafruit_dht
import adafruit_ssd1306
import board
import busio
import digitalio


def dht11(pin_number: int) -> adafruit_dht.DHT11:
	board_pin = getattr(board, f'D{pin_number}')
	return adafruit_dht.DHT11(board_pin)


def dht22(pin_number: int) -> adafruit_dht.DHT11:
	board_pin = getattr(board, f'D{pin_number}')
	return adafruit_dht.DHT22(board_pin)


def motion(pin_number: int) -> digitalio.DigitalInOut:
	board_pin = getattr(board, f'D{pin_number}')
	pir = digitalio.DigitalInOut(board_pin)
	pir.direction = digitalio.Direction.INPUT
	return pir


def button(pin_number: int) -> digitalio.DigitalInOut:
	board_pin = getattr(board, f'D{pin_number}')
	btn = digitalio.DigitalInOut(board_pin)
	btn.direction = digitalio.Direction.INPUT
	btn.pull = digitalio.Pull.UP
	return btn


def ssd1306(width, height) -> adafruit_ssd1306.SSD1306_I2C:
	# +1 since it is counting from 1 and not 0
	display = adafruit_ssd1306.SSD1306_I2C(
		width + 1, height + 1, busio.I2C(board.SCL, board.SDA)
	)
	return display
