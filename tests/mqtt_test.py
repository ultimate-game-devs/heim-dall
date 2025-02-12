import random
from time import sleep

from mqtt import MQTT

client1 = MQTT('10.174.207.237', str(random.randint(0, 9999)))
client1.publish('Code/Testing', 'Ich habe es geschafft')
client1.subscribe('Bash/ssh')

while client1.check_connection():
	sleep(0.1)
