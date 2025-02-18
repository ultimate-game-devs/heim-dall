from time import localtime

from inputDevices import DHT22

dht = DHT22(4)

while True:
	now = localtime()
	print(f'~~~ {now.tm_hour}:{now.tm_min}:{now.tm_sec} ~~~')
	dht_data = dht.get_data()
	if dht_data['temperature'] is not None and dht_data['humidity'] is not None:
		print(f'Temp - {dht_data["temperature"]}°C | Humid - {dht_data["humidity"]}%')
	else:
		raise 'Error: Temperature or Humidity None'
