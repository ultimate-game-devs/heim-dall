import time
import board
import digitalio

# Setup for PIR sensor (output from sensor)
pir = digitalio.DigitalInOut(board.D17)
pir.direction = digitalio.Direction.INPUT

previous_state = None
last_change_time = time.time()

while True:
    # Read current sensor state: True indicates motion, False indicates no motion
    current_state = pir.value
    current_time = time.time()

    # Calculate time difference since the last state change
    time_diff = current_time - last_change_time

    # Check for a change in state
    if current_state != previous_state:
        timestamp = time.strftime('%H:%M:%S', time.localtime(current_time))

        # Log the current time and new state
        state_str = "Motion Detected" if current_state else "No Motion"
        print(f"{timestamp} - {state_str} (Δ {time_diff:.2f} seconds)")

        last_change_time = current_time
        previous_state = current_state

    # Small delay for stability
    time.sleep(0.1)
