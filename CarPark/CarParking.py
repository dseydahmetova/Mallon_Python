from Lib.Car import *
import time, datetime
class CarParking:
    def __init__(self, numOfSpots):
        self.numOfSpots = numOfSpots
        self.listOfParkingSpaces = {}
        self.parkingDetails = {}
        for id in range(1, numOfSpots + 1):
            self.listOfParkingSpaces[id] = None
            self.parkingDetails[id] = {"paid": False, "parkingTime": None, "leavingTime": None, "payment": 2}

    def spaceIsOccupied(self, id):
        return self.listOfParkingSpaces[id] is not None

    def park(self, id, car):
        if not self.spaceIsOccupied(id):
            self.listOfParkingSpaces[id] = car
            # timestamp to calculate the bill
            self.parkingDetails[id]["parkingTime"] = datetime.datetime.now()
            parkingTime_formatted = self.parkingDetails[id]["parkingTime"].strftime("%m/%d/%Y, %H:%M:%S")
            print(f"Car with registration number {car} parked at space {id}. Time: {parkingTime_formatted}")
        else:
            print(f"Parking space {id} is already occupied.")

    def leave(self, id, car):
        if self.spaceIsOccupied(id) and self.listOfParkingSpaces[id] == car:
            if self.parkingDetails[id]["leavingTime"]:
                self.listOfParkingSpaces[id] = None
                self.parkingDetails[id]["paid"] = False
                print(f"Car with registration number {car.registration_num} left the space {id}.")
            else:
                print(f"Car with registration number {car.registration_num} has NOT payed for spot {id}.")
        else:
            print(f"Parking space id or car information doesn't match: {self.listOfParkingSpaces}")

    def pay(self, id, car):
        if self.spaceIsOccupied(id):
            self.parkingDetails[id]["paid"] = True
            # self.parkingDetails[id]["leavingTime"] = datetime.datetime.now()
            self.parkingDetails[id]["leavingTime"] = datetime.datetime(2024, 7, 31, 21, 25, 0, 0)
            timeDiff = self.parkingDetails[id]["leavingTime"] - self.parkingDetails[id]["parkingTime"]
            timeHours = int(round(timeDiff.total_seconds() / 3600))

            if timeHours <= 1:
                self.parkingDetails[id]["payment"]
            else:
                self.parkingDetails[id]["payment"] = self.parkingDetails[id]["payment"] * timeHours
            leavingTime_formatted = self.parkingDetails[id]["leavingTime"].strftime("%m/%d/%Y, %H:%M:%S")
            print(f"Car with registration number {car.registration_num} payed {self.parkingDetails[id]["payment"]} for spot {id}. Time: {leavingTime_formatted}")
        else:
            print(f"Parking space id or car information doesn't match: {self.listOfParkingSpaces}")

    def __str__(self):
        state = [f"Number of spots: {self.numOfSpots}"]
        for key in self.listOfParkingSpaces:
            if self.listOfParkingSpaces[key]:
                car_str = str(self.listOfParkingSpaces[key].registration_num)
                state.append(f"{key}: Reg_num: {car_str}, paid: {self.parkingDetails[key]["paid"]}, parking_time: {self.parkingDetails[key]["parkingTime"]}")
            else:
                state.append(f"{key}: Empty")
        return "\n".join(state)


# familyCar = FamilyCar(55, 65, 'KHTG06L', 8)
# luxuryCar = LuxuryCar(105, 185, 'HTCGF7L', 100000)
# sportCar = SportsCar(210, 200, 'PMF746L', 200000, "Toyota GR86")
# luxurySportsCar = LuxurySportsCar(100, 200, 'ATR746L', 130000, "LuxurySportsCar")
#
# print("-----------------Garage Info-----------------------")
#
# parkingGarage = CarParking(5)
# print(parkingGarage)
# print("\n---------------Parked the car-------------------------")
#
# # Calling function to park
# parkingGarage.park(1, sportCar)
# parkingGarage.park(2, luxuryCar)
# parkingGarage.park(3, familyCar)
#
# print("\n------------------Tried to park to the occupied space----------------------")
# parkingGarage.park(1, luxurySportsCar)
#
# print("\n---------------left the parking spot-------------------------")
# # Calling function to leave
# parkingGarage.leave(1, sportCar)

