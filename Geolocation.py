class Location:
	def __init__(self, lat: float, lng: float) -> None:
		self.lat = lat
		self.lng = lng


class GeolocationResult:
	def __init__(self, accuracy: int, location: Location) -> None:
		self.accuracy = accuracy
		self.location = location
