import socket
from typing import List

import adafruit_character_lcd.character_lcd as character_lcd
import adafruit_ssd1306
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont


def ili9341() -> None:
	pass


def ssd1306(pixel: List[tuple[int, int]]) -> None:
	i2c = busio.I2C(board.SCL, board.SDA)
	display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
	# Alternatively you can change the I2C address of the device with an addr parameter:
	# display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c, addr=0x31)

	# Clear the display. Always call show after changing pixels to make the display
	# update visible!
	display.fill(0)

	display.show()

	for i in range(len(pixel)):
		display.pixel(pixel[i][0], pixel[i][1], 1)

	# Set a pixel in the origin 0,0 position.
	# display.pixel(0, 0, 1)
	# Set a pixel in the middle 64, 16 position.
	# display.pixel(64, 16, 1)
	# # Set a pixel in the opposite 127, 31 position.
	# display.pixel(127, 31, 0)

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


def text_to_pixel_coordinates(text: str) -> List[tuple[int, int]]:
	font_height = 1000
	font_width = 1000
	font_path = 'fonts/Roboto-Regular.ttf'
	font_size = 20

	while font_width > 128 or font_height > 32:
		try:
			font = ImageFont.truetype(font_path, font_size)
		except IOError:
			raise IOError(f'Font file not found at path: {font_path}')

		bbox = font.getbbox(text)
		font_width = bbox[2] - bbox[0]
		font_height = bbox[3] - bbox[1]
		if font_width > 127 or font_height > 31:
			font_size -= 1

	image = Image.new('L', (128, 32))
	draw = ImageDraw.Draw(image)
	draw.text((0, 0), text, fill=255, font=font)

	image_width, image_height = image.size

	pixel = []
	for y in range(image_height):
		for x in range(image_width):
			value = image.getpixel((x, y))
			if value > 0:
				pixel.append((x, y))
	return pixel


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
co = text_to_pixel_coordinates(IPAddr)
ssd1306(co)
