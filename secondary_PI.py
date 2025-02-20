from time import sleep

from helper.inputDevices import DHT22
from helper.mqtt import MQTT

client = MQTT('10.103.48.1', 'secondary_PI')
dht = DHT22(4)

temperature: float = 10000000
humidity: float = 10000000

while True:
	data = dht.get_data()

	client.publish('outside/temperature', data['temperature'])
	client.publish('outside/humidity', data['humidity'])

	while not client.check_connection():
		client.reconnect()
	sleep(0.1)
