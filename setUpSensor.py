import adafruit_dht
import board

def setUpDHT11ONFour():
    return adafruit_dht.DHT11(board.D4)
