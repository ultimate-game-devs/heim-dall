import adafruit_character_lcd.character_lcd as character_lcd
import adafruit_ssd1306
import board
import busio
import digitalio


def ILI9341():
	pass


def SSD1306():
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
	display.pixel("Zeile 1", 0, 0, 1)
	display.pixel("Zeile 2", 0, 10, 1)
	display.pixel("Zeile 3", 0, 20, 1)
	# Set a pixel in the middle 64, 16 position.
	# display.pixel(64, 16, 1)
	# # Set a pixel in the opposite 127, 31 position.
	# display.pixel(127, 31, 1)
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


SSD1306()
