from setUpSensor import setUpDHT11ONFour

def getTemp(sensor) -> float | None:
    try:
        temperature = sensor.temperature
        sensor.exit()
        return temperature
    except Exception as error:
        print(error)
        return None
