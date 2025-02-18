from abc import ABC, abstractmethod
from typing import List

import adafruit_character_lcd.character_lcd as character_lcd
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont

import setup


class OutputDevice(ABC):
	@abstractmethod
	def __init__(self, pin_number: int) -> None:
		pass

	@abstractmethod
	def __exit__(self) -> None:
		pass


# @abstractmethod
# def get_data(self) -> None:
#     pass


class SSD1306(OutputDevice):
	def __init__(self) -> None:
		self.max_width = 127
		self.max_height = 31
		self.display = setup.ssd1306(self.max_width, self.max_height)

	def __exit__(self) -> None:
		self.resetDisplay()

	def resetDisplay(self) -> None:
		self.display.fill(0)
		self.display.show()

	def printOnDisplay(self, text: str):
		self.resetDisplay()
		cords = self.__text_to_pixel_coordinates(text)
		# self.display.pixel(64, 16, 1)
		for i in range(len(cords)):
			self.display.pixel(cords[i][0], cords[i][1], 1)
		self.display.show()

	def __text_to_pixel_coordinates(self, text: str) -> List[tuple[int, int]]:
		font_height = 1000
		font_width = 1000
		font_size = 1000
		font_path = 'fonts/Roboto-Regular.ttf'

		while font_width > self.max_width or font_height > self.max_height:
			try:
				font = ImageFont.truetype(font_path, font_size)
			except IOError:
				raise IOError(f'Font file not found at path: {font_path}')

			bbox = font.getbbox(text)
			font_width = bbox[2]
			font_height = bbox[3]

			if font_width > self.max_width or font_height > self.max_height:
				font_size -= 1

		image = Image.new('L', (self.max_width, self.max_height))
		draw = ImageDraw.Draw(image)
		draw.text((0, 0), text, fill=255, font=font)

		image_width, image_height = image.size

		pixel = []
		for y in range(image_height):
			for x in range(image_width):
				value = image.getpixel((x, y))
				if value > 50:
					pixel.append((x, y))
		return pixel


# def get_data(self) -> dht_data:
# 	return {'temperature': self.__get_temp(), 'humidity': self.__get_humid()}
#
# def __get_temp(self) -> float | None:
# 	try:
# 		return self.sensor.temperature
# 	except Exception as error:
# 		print(error)
# 		return None
#
# def __get_humid(self) -> float | None:
# 	try:
# 		return self.sensor.humidity
# 	except Exception as error:
# 		print(error)
# 		return None


class ILI9341(OutputDevice):
	def __init__(self, pin_number: int) -> None:
		pass

	def __exit__(self) -> None:
		pass


class LCD(OutputDevice):
	def __init__(self, pin_number: int) -> None:
		# TODO: Put setup into setup.py
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

		# TODO: Put write into its own message
		lcd.message = 'Hello\nCircuitPython'
		pass

	def __exit__(self) -> None:
		pass
