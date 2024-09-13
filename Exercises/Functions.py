myList = [1, 2, 3, 4, 5, 6, 7]
print(myList)
# Write a function that takes the last element in a list and moves it to the front of the list.
print('\n------------1------------')
def swap_el(list):
    last_el = list[-1]
    list.insert(0, last_el)
    list.pop(list[-1])
    return list

print("\nLast element first: ", swap_el(myList))

# Write a function that takes a list and a variable number of indices. The function should return a tuple of the values at those indices.
print('\n------------2------------')
def indices_el(list, num):
    newList = []
    for i in list:
        for j in num:
            if list.index(i) == j:
                newList.append(i)
    return tuple(newList)

indicesList = [0, 5, 2]
print(indicesList)
print("Element of given indices: ", indices_el(myList, indicesList))

# Write a function that takes named parameters and returns the parameters as a Dictionary of
# parameter name -> value
print('\n------------3------------')
def dictionary(keys, values):
    myDictionary = {}
    for key in keys:
        for value in values:
            myDictionary[key] = value
    return myDictionary

languages = ["python", "java", "c"]
years = [1991, 1195, 1972]
print("Dictionary: ", dictionary(languages,years))

print('\n------------------------')
def dictionary(**kwargs):
    for key in kwargs.keys():
        print(key, '->', kwargs[key])

dictionary(python = 1972, java = 1972, c = 1972)

# Write a function that take an initial value and a tuple of ints and accumulates into the initial value. For example,
# acc(0, (1,3,5)) should return 9.
print('\n------------4------------')
def acc(initialValue, tuple):
    sum = initialValue
    for num in tuple:
        sum += num
    return sum

print("Accumulate: ", acc(4, (5, 0, 11, 3)))

# Rewrite your Fibonacci exercise from the previous lab as a function. It should take an argument - how many numbers are required. For example,
# fib(5) #  should print # 1 1 2 3 5 the first five Fibonacci numbers. Test your code with the following calls:
# fib(2000)
# fib(100)
# fib(0)

print('\n------------5------------')

def print_fib(n):
    if n <= 0:
        print(0)
        return
    elif n == 1:
        print(1)
        return

    a,b = 0, 1
    while b <= n:
        print(b, '', end = '')
        # a =b and b= a+b
        a,b = b, a+b
    print()

print_fib(5)
print_fib(50)
print_fib(1)
print_fib(500)


print('\n------------6------------')
def fib(n):
    if n == 0:
        fib_list = []
    elif n == 1:
        fib_list = [0]
    elif n == 2:
        fib_list = [0, 1]
    else:
        a, b = 0, 1
        fib_list = []
        while b <= n:
            a, b = b, a + b
            fib_list.append(a)
    return fib_list

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(5))
print(fib(2000))
print(fib(100))

