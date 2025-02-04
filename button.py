import time
import board
import digitalio

button = digitalio.DigitalInOut(board.D23)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN

previous_state = button.value
last_change_time = time.time()

while True:
    current_state = button.value
    current_time = time.time()

    time_diff = current_time - last_change_time

    if current_state != previous_state:
        timestamp = time.strftime('%H:%M:%S', time.localtime(current_time))

        state_str = "Button Pressed" if not current_state else "Button no longer pressed"
        print(f"{timestamp} - {state_str} (Δ {time_diff:.2f} seconds)")

        last_change_time = current_time
        previous_state = current_state
