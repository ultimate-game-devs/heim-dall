import time

from inputDevices import Button
from mqtt import MQTT

button = Button(23)

previous_state = button.get_data()
last_change_time = time.time()

mqtt_client = MQTT('10.174.207.237', 'Dominik_PI')

while mqtt_client.check_connection():
	current_state = button.get_data()
	current_time = time.time()

	time_diff = current_time - last_change_time

	if current_state != previous_state:
		timestamp = time.strftime('%H:%M:%S', time.localtime(current_time))

		state_str = 'Button Pressed'
		if current_state:
			state_str = 'Button no longer pressed'

		print(f'{timestamp} - {state_str} (Δ {time_diff:.2f} seconds)')

		mqtt_client.publish(button, state_str)

		last_change_time = current_time
		previous_state = current_state

		time.sleep(0.2)
