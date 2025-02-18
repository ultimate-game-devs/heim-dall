import socket
from typing import Any

import adafruit_character_lcd.character_lcd as character_lcd
import adafruit_ssd1306
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont

FONT_PATH = 'fonts/Roboto-Regular.ttf'
FONT_SIZE = 20


def ili9341() -> None:
		pass


def ssd1306(cords: list[tuple[int | Any, int | Any]]) -> None:
		i2c = busio.I2C(board.SCL, board.SDA)
		display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
		# Alternatively you can change the I2C address of the device with an addr parameter:
		# display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)

		# Clear the display. Always call show after changing pixels to make the display
		# update visible!
		display.fill(0)

		display.show()

		# Set a pixel in the origin 0,0 position.
		# display.pixel(0, 0, 1)
		# Set a pixel in the middle 64, 16 position.
		# display.pixel(64, 16, 1)
		# # Set a pixel in the opposite 127, 31 position.
		# display.pixel(127, 31, 1)

		for i in range(len(cords)):
				display.pixel(cords[i][0], cords[i][1], 1)

		display.show()


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


def text_to_pixel_coordinates(
				text: str, offset: tuple[int, int] = (0, 0)
) -> list[tuple[int, int]]:
		try:
				font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
		except IOError:
				raise IOError(f'Font file not found at path: {FONT_PATH}')

		bbox = font.getbbox(text)
		width = int(round(bbox[2] - bbox[0], 0))
		height = int(round(bbox[3] - bbox[1], 0))

		image = Image.new('L', (width, height))
		draw = ImageDraw.Draw(image)
		draw.text((0, 0), text, fill=255, font=font)

		image_width, image_height = image.size

		cords = []
		for y in range(image_height):
				for x in range(image_width):
						if x > 128:
								print((x + offset[0], y + offset[1]))
								cords.append((x + offset[0], y + offset[1]))
		return cords


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
co = text_to_pixel_coordinates(IPAddr)
ssd1306(co)
