''' PROGRAM 9: Write a random number generator that generates random number between 1 and 6 '''

import random
print("Dice game")
print("Game starts")
ans = 'y'
while ans == 'y':
    print("Dice rolling")
    s = random.randint(1,6)
    print("Your roll is ", s)
    ans = input("Do you want to roll again? (y/n)")
if ans != 'y':
    print("The entered value is invalid")
print("See you again!")

''' FRIENDLY REMINDER TO WRITE THE SAMPLE OUTPUT '''
