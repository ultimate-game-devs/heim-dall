import time
from time import sleep

from helper.inputDevices import DHT22, Motion, Button
from helper.mqtt import MQTT
from helper.outputDevices import SSD1306

# Setup components
display = SSD1306()
motion = Motion(17)
dht = DHT22(4)
button = Button(23)

text: str = ''
old_text: str = ''
show: str = 'temperature'

client = MQTT('10.103.48.1', 'main_PI')

while True:
	movement = motion.get_data()
	if not movement:
		continue

	while movement:
		pressed = button.get_data()
		temp_humid = dht.get_data()

		if not pressed:
			match show:
				case 'inside_temperature':
					show = 'humidity'
				case 'inside_humidity':
					show = 'outside_temperature'
				case 'outside_temperature':
					if client.check_connection():
						show = 'outside_humidity'
					else:
						show = 'clock'
				case 'outside_humidity':
					show = 'clock'
				case 'clock':
					show = 'inside_temperature'
				case _:
					show = 'inside_temperature'

		match show:
			case 'inside_temperature':
				text = f"In: {str(temp_humid['temperature'])}°C"
			case 'inside_humidity':
				text = f"In: {str(temp_humid['humidity'])}%"
			case 'outside_temperature':
				if client.check_connection():
					show = (
						f"Out: "
	          f"{client.simple_subscribtion('outside/temperature').payload.decode()}°C"
					)
				else:
					show = "No connection to other PI"
			case 'outside_humidity':
				if client.check_connection():
					show = (
						f"Out: "
						f"{client.simple_subscribtion('outside/humidity').payload.decode()}%"
					)
				else:
					show = "No connection to other PI"
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
