class Car(object):
    def __init__ (self, speed, top_speed, registration_num):
        self.speed = speed
        self.top_speed = top_speed
        self.registration_num = registration_num

    def __str__(self):
        return f"speed: {self.speed}, top_speed: {self.top_speed}, number: {self.registration_num}"

    # @classmethod
    def accelerate(self):
        newSpeed = self.speed + 15
        if(newSpeed > self.top_speed):
            print("Warning!")
        return newSpeed


car1 = Car(30, 45, "12JL5")
print("Car object: ", car1)
print("Modified speed: ", car1.accelerate())