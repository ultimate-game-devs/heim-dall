import os
import random

import paho.mqtt.client as mqtt
from dotenv import load_dotenv


class MQTT:
	def __init__(self, broker: str, client_name: str) -> None:
		# Set Up Client
		self.__client = mqtt.Client(client_name)

		# Binding callbacks
		self.__client.on_connect = self.__on_connect
		self.__client.on_message = self.__on_message

		# Starting the client
		self.__client.connect(broker)
		self.__client.loop_start()

	def __exit__(self) -> None:
		self.__client.loop_stop()
		self.__client.disconnect()

	# Callback functions
	def __on_connect(self, client, userdata, flags, rc) -> None:
		if rc == 0:
			print('connected')
			print(f'client {client}')
			print(f'userdata {userdata}')
			print(f'flags {flags}')
			print(f'rc {rc}')
		else:
			print(f'Bad connection | Return code: {rc}')  #

	def __on_message(self, client, userdata, msg) -> None:
		pass


load_dotenv()

username = os.getenv('MQTT_Username')
print(username)

client1 = MQTT('192.168.111.111', f'Python Code {random.randint}')
