from abc import ABC,abstractmethod

class Ride(ABC):

    def __init__(self,passenger_name,distance_km):
        self.passenger_name = passenger_name
        self.__distance_km = distance_km

    def get_distance(self):
        return self.__distance_km 

    @abstractmethod
    def calculate_fare(self):
        pass

class BikeRide(Ride):

    def __init__(self, passenger_name, distance_km,vehicle_number):
        super().__init__(passenger_name, distance_km)
        self.vehicle_number = vehicle_number

    def calculate_fare(self):
         fare = 20 + (8 * self.get_distance())
         return fare
        

class CarRide(Ride):

    def __init__(self, passenger_name, distance_km,vehicle_number):
        super().__init__(passenger_name, distance_km)
        self.vehicle_number = vehicle_number

    def calculate_fare(self):
         fare = 50 + (15 * self.get_distance())
         return fare

def print_receipt(ride):
    print(f"Passenger: {ride.passenger_name}")
    print(f"Vehicle Number: {ride.vehicle_number}")
    print(f"Distance: {ride.get_distance()} km")
    print(f"Total Fare: {ride.calculate_fare()}")
    print("--------------------")
        

bike = BikeRide("Rahul", 5, "WB01AB1234")
car = CarRide("Priya", 5, "WB02CD5678")

print_receipt(bike)
print_receipt(car)
    
        

    
        