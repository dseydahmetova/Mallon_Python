import random

num = random.randint(100,200)

i = 3;
while i > 0:
    print('You have', ' ', i, ' ', 'attempts')
    guess = int(input('Enter the number between 100 and 200:'))
    if num == guess:
        print("You guessed number")
        break
    else:
        i -= 1
        print("Try again")

print("The number was: ", num)