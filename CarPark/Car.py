from abc import ABCMeta, abstractmethod

# Car abstract class
class Car(metaclass=ABCMeta):
    def __init__(self, speed, top_speed, registration_num):
        self.speed = speed
        self.top_speed = top_speed
        self.registration_num = registration_num

    def __str__(self):
        return f"speed: {self.speed}, top_speed: {self.top_speed}, number: {self.registration_num}"

    def accelerate(self):
        newSpeed = self.speed + 15
        if newSpeed > self.top_speed:
            print("Warning! Your speed is over ", self.top_speed)
        return newSpeed

    @abstractmethod
    def engineInfo(self): pass


# Family car child class
class FamilyCar(Car):
    def __init__(self, speed, top_speed, registration_num, seat_num):
        super().__init__(speed, top_speed, registration_num)
        self.seat_num = seat_num

    def __str__(self):
        seat = f"seat_number: {self.seat_num}"
        return ', '.join([super().__str__(), seat])

    def accelerate(self):
        super().accelerate()

    def engineInfo(self):
        print("Typical family car engine: 1.5L - 2.5L")

# Luxury car child class
class LuxuryCar(Car):
    def __init__(self, speed, top_speed, registration_num, price):
        super().__init__(speed, top_speed, registration_num)
        self.price = price

    def __str__(self):
        price = f"price: {self.price}"
        return ', '.join([super().__str__(), price])

    def engineInfo(self):
        print("Luxury car engine: Smooth and powerful, often with turbochargers")


# Sports car child class
class SportsCar(Car):
    def __init__(self, speed, top_speed, registration_num, price, model):
        super().__init__(speed, top_speed, registration_num)
        self.price = price
        self.model = model

    def __str__(self):
        price = f"price: {self.price}"
        model = f"model: {self.model}"
        return ', '.join([super().__str__(), price, model])

    def accelerate(self):
        super().accelerate()

    def engineInfo(self):
        print("Powered by a 2.4-liter horizontally opposedfour-cylinder engine")


# Luxury Sports Car car child class
class LuxurySportsCar(Car):
    def __init__(self, speed, top_speed, registration_num, price, model):
        super().__init__(speed, top_speed, registration_num)
        self.price = price
        self.model = model

    def __str__(self):
        price = f"price: {self.price}"
        model = f"model: {self.model}"
        return ', '.join([super().__str__(), price, model])

    def accelerate(self):
        super().accelerate()

    def engineInfo(self):
        print("490 - 670 horsepower")



# familyCar = FamilyCar(55, 65, 'KHTG06L', 8)
# print("\nfamilyCar:", familyCar)
# familyCar.accelerate()
# print("----------------------------------------")
# luxuryCar = LuxuryCar(105, 185, 'HTCGF7L', 100000)
# print("luxuryCar:", luxuryCar)
# luxuryCar.accelerate()
# print("----------------------------------------")
# sportCar = SportsCar(210, 200, 'PMF746L', 200000, "Toyota GR86")
# print("sportCar:", sportCar)
# sportCar.accelerate()
# sportCar.engineInfo()
# print("----------------------------------------")
# luxurySportsCar = LuxurySportsCar(100, 200, 'ATR746L', 130000, "LuxurySportsCar")
# print("luxurySportsCar:", luxurySportsCar)
# luxurySportsCar.accelerate()
# luxurySportsCar.engineInfo()
# print("----------------------------------------")
