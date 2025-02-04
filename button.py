import time
import board
import digitalio

button = digitalio.DigitalInOut(board.D23)
button.direction = digitalio.Direction.INPUT

previous_state = None
last_change_time = time.time()

while True:
    # Read current sensor state: True indicates press, False indicates no press
    current_state = button.value
    current_time = time.time()

    # Calculate time difference since the last state change
    time_diff = current_time - last_change_time

    # Check for a change in state
    if current_state != previous_state:
        timestamp = time.strftime('%H:%M:%S', time.localtime(current_time))

        # Log the current time and new state
        state_str = "Button Pressed" if current_state else "Button no longer pressed"
        print(f"{timestamp} - {state_str} (Δ {time_diff:.2f} seconds)")

        last_change_time = current_time
        previous_state = current_state
