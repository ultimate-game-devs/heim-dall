from gpiozero import OutputDevice

temp = OutputDevice(4)

print("value" + str(temp.value))
print("source" + temp.source)
