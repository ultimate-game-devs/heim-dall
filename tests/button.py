import time

from inputDevices import Button

button = Button(23)

previous_state = button.get_data()
last_change_time = time.time()

while True:
	current_state = button.get_data()
	current_time = time.time()

	time_diff = current_time - last_change_time

	if current_state != previous_state:
		timestamp = time.strftime('%H:%M:%S', time.localtime(current_time))

		state_str = 'Button Pressed'
		if current_state:
			'Button no longer pressed'

		print(f'{timestamp} - {state_str} (Δ {time_diff:.2f} seconds)')

		last_change_time = current_time
		previous_state = current_state

		time.sleep(0.2)
