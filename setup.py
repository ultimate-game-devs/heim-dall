import adafruit_character_lcd.character_lcd as character_lcd
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


def ssd1306(width: int, height: int) -> adafruit_ssd1306.SSD1306_I2C:
	# +1 since it is counting from 1 and not 0
	return adafruit_ssd1306.SSD1306_I2C(
		width + 1, height + 1, busio.I2C(board.SCL, board.SDA)
	)


def lcd(rs_pin: int, en_pin: int, d7_pin: int, d6_pin: int, d5_pin: int, d4_pin: int, columns: int,
        rows: int) -> adafruit_character_lcd.character_lcd:
	lcd_rs = digitalio.DigitalInOut(getattr(board, f'D{rs_pin}'))  # 26
	lcd_en = digitalio.DigitalInOut(getattr(board, f'D{en_pin}'))  # 19
	lcd_d7 = digitalio.DigitalInOut(getattr(board, f'D{d7_pin}'))  # 27
	lcd_d6 = digitalio.DigitalInOut(getattr(board, f'D{d6_pin}'))  # 22
	lcd_d5 = digitalio.DigitalInOut(getattr(board, f'D{d5_pin}'))  # 24
	lcd_d4 = digitalio.DigitalInOut(getattr(board, f'D{d4_pin}'))  # 25

	# columns: 16
	# rows: 2

	return character_lcd.Character_LCD_Mono(
		lcd_rs,
		lcd_en,
		lcd_d4,
		lcd_d5,
		lcd_d6,
		lcd_d7,
		columns,
		rows,
	)
