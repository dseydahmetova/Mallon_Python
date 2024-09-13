from Lib.Car import *
from Lib.CarParking import *

def main():
    car = None
    garage = None
    cars = []

    while True:
        print("\nWelcome to Parking Garage")
        print("1. Create Parking Garage")
        print("2. Create Car")
        print("3. Park Car")
        print("4. Remove Car")
        print("5. View Parking Garage")
        print("6. Pay for Parking")
        print("7. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            num = int(input("Enter the number of parking spaces: "))
            garage = CarParking(num)
            print(f"Created a parking garage with {num} spaces.")
        if choice == "2":
            print("\n1. A Family Car")
            print("2. A Luxury Car")
            print("3. A Sports Car")
            print("4. A Luxury Sports Car")
            carType = str(input("Enter the type of the car: "))

            if carType == "1":
                car = FamilyCar(55, 65, 'KHTG06L', 8)
            elif carType == "2":
                car = LuxuryCar(105, 185, 'HTCGF71', 100000)
            elif carType == "3":
                car = SportsCar(210, 200, 'PMF746P', 200000, "Toyota GR86")
            elif carType == "4":
                car = LuxurySportsCar(100, 200, 'ATR746T', 130000, "LuxurySportsCar")
            else:
                print("Invalid car type.")
                continue
            cars.append(car)
            print(f"Created a car: {car}")
        if choice == "3":
            if garage is None and car is None:
                print("Create a garage and car first")
            else:
                id = int(input("Enter the id of parking spaces: "))
                regNum = str(input("Enter the car reg_number: "))
                found = False
                for car in cars:
                    if car.registration_num == regNum:
                        if car in garage.listOfParkingSpaces.values():
                            print("Car is already parked")
                            found = True
                        else:
                            garage.park(id, car)
                            found = True
                        break
                if not found:
                    print(f"Car with plate number {regNum} not found")
        if choice == "4":
            if garage is None and car is None:
                print("Create a garage and car first")
            else:
                id = int(input("Enter the id of parking spaces: "))
                regNum = str(input("Enter the car reg_number: "))
                found = False
                for car in cars:
                    if car.registration_num == regNum:
                        if car in garage.listOfParkingSpaces.values():
                            garage.leave(id, car)
        if choice == "5":
            if garage is None:
                print("Create a garage first")
            else:
                print(garage)
        if choice == "6":
            if garage is None and car is None:
                print("Create a garage and car first")
            else:
                id = int(input("Enter the id of parking spaces: "))
                garage.pay(id, car)
        if choice == "7":
            exit()

if __name__ == "__main__":
    main()