import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(4, GPIO.OUT)

event = GPIO.event_detected(4)

print(event)
