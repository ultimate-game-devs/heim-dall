from setUpSensor import setUpDHT11ONFour

def getHumid() -> float | None:
    try:
        sensor = setUpDHT11ONFour()
        humidity = sensor.humidity
        sensor.exit()
        return humidity
    except Exception as error:
        print(error)
        return None
