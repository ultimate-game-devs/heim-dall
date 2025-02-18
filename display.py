import socket

import adafruit_character_lcd.character_lcd as character_lcd
import board
import digitalio

from outputDevices import SSD1306


def ili9341() -> None:
	pass


def lcd() -> None:
	lcd_rs = digitalio.DigitalInOut(board.D26)
	lcd_en = digitalio.DigitalInOut(board.D19)
	lcd_d7 = digitalio.DigitalInOut(board.D27)
	lcd_d6 = digitalio.DigitalInOut(board.D22)
	lcd_d5 = digitalio.DigitalInOut(board.D24)
	lcd_d4 = digitalio.DigitalInOut(board.D25)

	lcd_columns = 16
	lcd_rows = 2

	lcd = character_lcd.Character_LCD_Mono(
		lcd_rs,
		lcd_en,
		lcd_d4,
		lcd_d5,
		lcd_d6,
		lcd_d7,
		lcd_columns,
		lcd_rows,
	)

	lcd.message = 'Hello\nCircuitPython'


display = SSD1306()

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

display.printOnDisplay(IPAddr)
