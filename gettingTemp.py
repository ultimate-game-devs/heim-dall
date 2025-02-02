from setUpSensor import setUpDHT11ONFour

def getTemp() -> float | None:
    try:
        sensor = setUpDHT11ONFour()
        temperature = sensor.temperature
        sensor.exit()
        return temperature
    except Exception as error:
        print(error)
        return None
