import os
import random
from time import sleep

import paho.mqtt.client as mqtt
from dotenv import load_dotenv


class MQTT:
	def __init__(self, broker: str, client_name: str) -> None:
		# Getting username and password from the env
		load_dotenv()
		username = os.getenv('MQTT_Username')
		password = os.getenv('MQTT_Password')

		# Set Up Client
		self.__client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_name)
		self.__client.username_pw_set(username, password)

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
	def __on_connect(self, client, userdata, flags, reason_code, properties):
		if flags.session_present:
			print(f'Session is resumed or something | flags {flags}')
		if reason_code == 0:
			print('Connected to Server')
		else:
			print(f'Bad connection | reason_code {reason_code}')

	def __on_message(self, client, userdata, message) -> None:
		pass

	# Other Functions
	def publish(self, message):
		pass


client1 = MQTT('192.168.111.111', f'Python Code {random.randint}')
sleep(10)
