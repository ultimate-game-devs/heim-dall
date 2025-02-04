import time
import board
import digitalio

# Setup for PIR sensor (output from sensor)
pir = digitalio.DigitalInOut(board.D17)
pir.direction = digitalio.Direction.INPUT

# Setup for LED (output to LED)
led = digitalio.DigitalInOut(board.D18)
led.direction = digitalio.Direction.OUTPUT
led.value = False

while True:
    # Read current sensor state: True indicates motion, False indicates no motion
    current_state = pir.value
    led.value = current_state

    # Check for a change in state
    if current_state != previous_state:
        # Log the current time and new state
        state_str = "Motion Detected" if current_state else "No Motion"
        print(f"{time.strftime('%H:%M:%S')} - {state_str}")
        previous_state = current_state

    # Small delay for stability
    time.sleep(0.1)
