from abc import ABC, abstractmethod
from typing import List

from PIL import Image, ImageDraw, ImageFont

import setup


class OutputDevice(ABC):
	@abstractmethod
	def __init__(self, pin_number: int) -> None:
		pass

	@abstractmethod
	def __exit__(self) -> None:
		pass


class SSD1306(OutputDevice):
	def __init__(self) -> None:
		self.max_width = 127
		self.max_height = 31
		self.display = setup.ssd1306(self.max_width, self.max_height)

	def __exit__(self) -> None:
		self.__reset_display()

	def print_on_display(self, text: str) -> None:
		self.__reset_display()
		cords = self.__text_to_pixel_coordinates(text)
		for i in range(len(cords)):
			self.display.pixel(cords[i][0], cords[i][1], 1)
		self.display.show()

	def __reset_display(self) -> None:
		self.display.fill(0)
		self.display.show()

	def __text_to_pixel_coordinates(self, text: str) -> List[tuple[int, int]]:
		font_height = 1000
		font_width = 1000
		font_size = 1000
		font_path = '../fonts/Roboto-Regular.ttf'

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


# Idk, how to set it up | but we physically have one
# class ILI9341(OutputDevice):
# 	def __init__(self, pin_number: int) -> None:
# 		pass
#
# 	def __exit__(self) -> None:
# 		pass


class LCD(OutputDevice):
	def __init__(self, rs: int, en: int, seven: int, six: int, five: int, four: int, columns: int, rows: int) -> None:
		self.display = setup.lcd(rs, en, seven, six, five, four, columns, rows)

	def __exit__(self) -> None:
		self.display.clear()
		pass

	def writeToDisplay(self, text: str):
		self.display.message = text
