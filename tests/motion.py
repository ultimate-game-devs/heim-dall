import time

from inputDevices import Motion

# Setup for PIR sensor (output from sensor)
pir = Motion(17)

previous_state = None
last_change_time = time.time()

while True:
    # Read current sensor state: True indicates motion, False indicates no motion  # noqa: ERA001, E501
    current_state = pir.get_data()
    current_time = time.time()

    # Calculate time difference since the last state change
    time_diff = current_time - last_change_time

    # Check for a change in state
    if current_state != previous_state:
        timestamp = time.strftime('%H:%M:%S', time.localtime(current_time))

        # Log the current time and new state
        state_str = 'Motion Detected' if current_state else 'No Motion'
        print(f'{timestamp} - {state_str} (Δ {time_diff:.2f} seconds)')

        last_change_time = current_time
        previous_state = current_state

    # Small delay for stability
    time.sleep(0.1)
