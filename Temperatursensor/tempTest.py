import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

func = GPIO.gpio_function(4)

print(func)
