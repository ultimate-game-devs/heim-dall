from gpiozero import InputDevice

temp = InputDevice(4)

print("value" + str(temp.value))
