import calculation

def main():
    n = 7
    if n % 2 == 0:
        print(calculation.subtractOne(n))
    else:
        print(calculation.addOne(n))

print("Doc: ", calculation.__doc__)
print("Name: ", calculation.__name__)
print("Dir: ", dir(calculation))

# Call the main() function directly
calculation.main()

# Dynamically call the main() function
module_name = "calculation"
main_function_name = "main"

# Import the module dynamically
example_module = __import__(module_name)
getattr(example_module, main_function_name)()

# Call the main() function using if __name__ == "__main__"
if __name__ == "__main__":
    calculation.main()
