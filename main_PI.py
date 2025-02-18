from time import sleep

from helper.inputDevices import DHT22, Motion, Button
from helper.outputDevices import SSD1306

# Setup components
display = SSD1306()
motion = Motion(17)
dht = DHT22(4)
button = Button(23)

text: str = ''
oldText: str = ''
show_temp = True

while True:
	movement = motion.get_data()
	if not movement:
		continue

	while movement:
		pressed = button.get_data()
		temp_humid = dht.get_data()

		if not pressed:
			show_temp = not show_temp

		if show_temp:
			text = str(temp_humid['temperature']) + '°C'
		else:
			text = str(temp_humid['humidity']) + '%'

		if text != oldText:
			display.print_on_display(text)

		movement = motion.get_data()
		oldText = text
		sleep(0.2)
	display.clear_display()
