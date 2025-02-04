import time
import board
import digitalio

# Setup for PIR sensor (output from sensor)
pir_sensor = digitalio.DigitalInOut(board.D17)
pir_sensor.direction = digitalio.Direction.INPUT

# Setup for LED (output to LED)
led = digitalio.DigitalInOut(board.D18)
led.direction = digitalio.Direction.OUTPUT

# Setup for button (to toggle sensor on/off)
# button = digitalio.DigitalInOut(board.D23)
# button.direction = digitalio.Direction.INPUT
# button.pull = digitalio.Pull.UP  # Enable internal pull-up resistor

# Variable to keep track of sensor state (enabled/disabled)
# sensor_enabled = True
# print("System started. Sensor enabled:", sensor_enabled)

while True:
    # Check for button press (active low)
    # if not button.value:  # Button is pressed
    #     sensor_enabled = not sensor_enabled  # Toggle sensor state
    #     print("Sensor enabled:", sensor_enabled)
    #     # Debounce delay to avoid multiple toggles on one press
    #     time.sleep(0.5)
    #
    # # When sensor is enabled, check PIR sensor output
    # if sensor_enabled:
        if pir_sensor.value:  # PIR sensor has detected motion
            led.value = True
        else:
            led.value = False
    # else:
    #     # When disabled, ensure LED is off regardless of sensor state
    #     led.value = False

    # time.sleep(0.1)  # Short delay for stable reading
