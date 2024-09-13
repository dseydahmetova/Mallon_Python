class Calculator(object):
    def __init__(self):
        self.memory = None

    def add(self, num1, num2):
        result = num1 + num2
        self.memory = result
        return result

    def sub(self, num1, num2):
        result = num1 - num2
        self.memory = result
        return result

    def mult(self, num1, num2):
        result = num1 * num2
        self.memory = result
        return result

    def div(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError("Can not divide to 0")
        result =  num1 / num2
        self.memory = result
        return result

    def cleanMemory(self):
        self.memory = None



# def main():
#     a = 7
#     b = 4
#     print(add(a, b))
#
# if __name__ == "__main__":
#     main()