class Location:
    def __init__(self,lat,lng):
        self.lat = lat
        self.lng = lng


class GeolocationResult:
    def __init__(self,accuracy,location:Location):
        self.accuracy = accuracy
        self.location = location
    
