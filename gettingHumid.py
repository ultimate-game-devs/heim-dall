from setUpSensor import setUpDHT11ONFour

def getHumid(sensor) -> float | None:
    try:
        humidity = sensor.humidity
        sensor.exit()
        return humidity
    except Exception as error:
        print(error)
        return None
