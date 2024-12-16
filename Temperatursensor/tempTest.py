import gpio as GPIO

GPIO.setup(7, GPIO.OUT)

print(GPIO.read(7))