import os
import random
from time import sleep

import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from paho.mqtt.client import Client, ConnectFlags
from paho.mqtt.properties import Properties
from paho.mqtt.reasoncodes import ReasonCode


class MQTT:
	def __init__(self, broker: str, client_name: str) -> None:
		print('Client Name', client_name)
		self.__client_name = client_name

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
		sleep(0.5)

		# Subscribing to the topic that will exit the client
		self.subscribe(client_name)

	def __exit__(self) -> None:
		self.__client.loop_stop()
		self.__client.disconnect()

	# Callback functions
	def __on_connect(
		self,
		client: Client,
		userdata: any,
		flags: ConnectFlags,
		reason_code: ReasonCode,
		properties: Properties,
	) -> None:
		if flags.session_present:
			print(f'Session is resumed or something | flags {flags}')
		if reason_code == 0:
			print('Connected to Server')
		else:
			print(f'Bad connection | reason_code {reason_code}')

	def __on_message(
		self, client: Client, userdata: any, message: mqtt.MQTTMessage
	) -> None:
		# Connection to db to save Data - maybe not needed
		if message.topic == self.__client_name:
			if message.payload == b'kill':
				print('The client now kills itself')
				self.__exit__()
			else:
				return
		print(
			f'Recived message on {message.topic} '
			f'with the id {message.mid} at {message.timestamp}.'
			f'The message is {message.payload}',
		)

	# Other Functions
	def publish(self, topic: str, message: str | bytes | bytearray | int | float) -> bool:
		try:
			message_info = self.__client.publish(topic, message)
			message_info.wait_for_publish()
			print(f'Message has been published as {message_info.mid}')
			return True
		except Exception as error:
			print(error)
			return False

	def subscribe(self, topic: str) -> bool:
		subreturn = self.__client.subscribe(topic)
		if subreturn[0] == mqtt.MQTT_ERR_SUCCESS:
			print(f'Successfuly subscribed to {topic} with the id {subreturn[1]}')
			return True
		print(f'Something went wrong when subscribing | Error Code {subreturn[0]}')
		return False

	def check_connection(self) -> bool:
		return self.__client.is_connected()


client1 = MQTT('192.168.111.111', str(random.randint(0, 9999)))
client1.publish('Code/Testing', 'Ich habe es geschafft')
client1.subscribe('Bash/ssh')

while client1.check_connection():
	sleep(0.1)
