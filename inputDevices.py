from abc import ABC, abstractmethod
from typing import TypedDict

import setUp

dht_data = TypedDict(
	'dht_data', {'temperature': float | None, 'humidity': float | None}
)


class InputDevice(ABC):
	@abstractmethod
	def __init__(self, pin_number: int) -> None:
		pass

	@abstractmethod
	def __exit__(self) -> None:
		pass

	@abstractmethod
	def get_data(self) -> None:
		pass


class DHT11(InputDevice):
	def __init__(self, pin_number: int) -> None:
		self.sensor = setUp.dht11(pin_number)

	def __exit__(self) -> None:
		self.sensor.exit()

	def get_data(self) -> dht_data:
		return {'temperature': self.__get_temp(), 'humidity': self.__get_humid()}

	def __get_temp(self) -> float | None:
		try:
			return self.sensor.temperature
		except Exception as error:
			print(error)
			return None

	def __get_humid(self) -> float | None:
		try:
			return self.sensor.humidity
		except Exception as error:
			print(error)
			return None


class Motion(InputDevice):
	def __init__(self, pin_number: int) -> None:
		self.sensor = setUp.motion(pin_number)

	def __exit__(self) -> None:
		self.sensor.deinit()

	def get_data(self) -> bool:
		return self.sensor.value


class Button(InputDevice):
	def __init__(self, pin_number: int) -> None:
		self.button = setUp.button(pin_number)

	def __exit__(self) -> None:
		self.button.deinit()

	def get_data(self) -> bool:
		return self.button.value
