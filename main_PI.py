import time
from time import sleep

from helper.inputDevices import DHT22, Motion, Button
from helper.outputDevices import SSD1306

# Setup components
display = SSD1306()
motion = Motion(17)
dht = DHT22(4)
button = Button(23)

text: str = ''
old_text: str = ''
show: str = 'temperature'

while True:
	movement = motion.get_data()
	if not movement:
		continue

	while movement:
		pressed = button.get_data()
		temp_humid = dht.get_data()

		if not pressed:
			match show:
				case 'temperature':
					show = 'humidity'
				case 'humidity':
					show = 'clock'
				case 'clock':
					show = 'temperature'
				case _:
					show = 'temperature'

		match show:
			case 'temperature':
				text = str(temp_humid['temperature']) + '°C'
			case 'humidity':
				text = str(temp_humid['humidity']) + '%'
			case 'clock':
				now = time.localtime()
				text = (
					f'{now.tm_hour if len(str(now.tm_hour)) == 2 else "0" + str(now.tm_hour)}:'
					f'{now.tm_min if len(str(now.tm_min)) == 2 else "0" + str(now.tm_min)}:'
					f'{now.tm_sec if len(str(now.tm_sec)) == 2 else "0" + str(now.tm_sec)}'
				)

		if text != old_text:
			display.print_on_display(text)

		movement = motion.get_data()
		old_text = text
		sleep(0.2)
	display.clear_display()
