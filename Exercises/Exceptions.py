class NumOutOfRangeError(ValueError):
    """ Number has to be between 0 and 9999"""

class InvalidTypeError(ValueError):
    """ String found, Please enter a valid integer"""

def div_numbers():
    min = 0
    max = 9999
    try:
        num1 = input(f"Enter a number1 between {min} and {max}: ")
        num2 = input(f"Enter a number2 between {min} and {max}: ")
        try:
            num1 = int(num1)
            num2 = int(num2)
        except Exception as d:
            raise InvalidTypeError() from d
        else:
            if (num1 >= min and num1 < max) and (num2 > min and num2 < max):
                div = num1 / num2
                print(div)
            else:
                raise NumOutOfRangeError()
    except InvalidTypeError as e:
        print(f"Error: {e.__doc__}")
    except NumOutOfRangeError as e:
        print(f"Error: {e.__doc__}")


div_numbers()






