from helper.outputDevices import SSD1306

display = SSD1306()

text = ''

while True:
	display.print_on_display(input())
