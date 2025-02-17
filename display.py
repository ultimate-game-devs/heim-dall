import socket
from typing import Any

import adafruit_character_lcd.character_lcd as character_lcd
import adafruit_ssd1306
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont


def ILI9341():
	pass


def SSD1306(coords: list[tuple[int | Any, int | Any]]):
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

	for i in range(len(coords)):
		display.pixel(coords[i][0], coords[i][1], 1)

	display.show()


def lcd():
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


def text_to_pixel_coordinates(text, font_path, font_size, offset=(0, 0)) -> list[tuple[int, int]]:
	try:
		font = ImageFont.truetype(font_path, font_size)
	except IOError:
		raise IOError(f"Font file not found at path: {font_path}")

	# Get an initial size (could be slightly too small)
	try:
		width, height = font.getsize(text)
	except AttributeError:
		bbox = font.getbbox(text)
		width = bbox[2] - bbox[0]
		height = bbox[3] - bbox[1]

	# Create a slightly larger image
	image = Image.new('L', (width, height + 10), color=0)  # 4 extra pixels in height
	draw = ImageDraw.Draw(image)
	draw.text((0, 0), text, fill=255, font=font)

	# Crop to the bounding box of drawn text (optional)
	cropped = image.crop(image.getbbox())

	cropped_width, cropped_height = cropped.size
	coords = []
	for y in range(cropped_height):
		for x in range(cropped_width):
			if cropped.getpixel((x, y)) > 128:
				coords.append((x + offset[0], y + offset[1]))
	return coords

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
co = text_to_pixel_coordinates("IPAddr", "fonts/Roboto-Regular.ttf", 16)
SSD1306(co)
