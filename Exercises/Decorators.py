from time import gmtime, strftime

def logging_fun(func):
    print("The user logged in:")
    def wrapper(value):
        print('Logged in at: ')
        return func(value)
    return wrapper

@logging_fun
def print_value(value):
    return value

def main():
    now = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
    print(print_value(now))
    print('Done')

if __name__ == '__main__':
    main()

