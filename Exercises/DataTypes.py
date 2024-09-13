print('-----------1-2-------------')
print(type(5))
print(type(5000 * 50000000))
print(type('j'))
print(type(1j))
print(type((1,)))
print(type([1]))
print(type(None))
print('------------3------------')

print(0.1 + 0.1 + 0.1 - 0.3)
print(0.1 + 0.1 + 0.1)
print('------------------------')
from decimal import *
print(Decimal(".1") + Decimal(".1") + Decimal(".1") - Decimal(".3"))
print(Decimal(".1") + Decimal(".1") + Decimal(".1"))

print('------------4------------')
n = 5
a = 1
b = 1
print(a, b, end = " ")
for i in range(2, n):
        c = a + b
        print(c, end = " ")
        a = b
        b = c




print('\n------------5------------')
name = "Dana"
for i in name[:-1]:
    print(i, '', sep = ":", end = '')
print(name[-1], end = '')


print('\n------------additional------------')
l = [1, 2, 3, 4, 5, 6]
print(l[3::-1])
print(l[1:2])

print('\n------------extension------------')

myList = [1, 4, 9, 16, 25]
oddNum = [x for x in myList if x % 2 == 1]
print(oddNum)

print('\n------------6------------')
count = 0
myList = (input("Enter 10 numbers between 1 and 8: ").split())
if (len(myList) != 10):
    myList = (input("Not 10 numbers. Please try again. Enter 10 numbers between 1 and 8: ").split())
else:
    for i in myList:
        if int(i) in range(1, 9):
            if int(i) == 5:
                count += 1
        else:
            myList = (input("Out of range. Try again: ").split())
print('Number of 5s: ', count)


