from gpiozero import OutputDevice

temp = OutputDevice(4)

print("values" + temp.values)
print("value" + temp.value)
print("source" + temp.source)
