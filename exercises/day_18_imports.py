from fractions import Fraction
from math import fsum
import random as rn

# 1) Import the fractions module and create a Fraction from the float 2.25.
print(Fraction(2.25))

# 2) Import only the fsum function from the math module and use it to find the sum of the following series of floats:
numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
result =  fsum(numbers)
print(result)



# 3) Import the random module using an alias, and find a random number between 1 and 100 using the randint function.
print(rn.randint(1,100))


# 4) Use the randint function from the exercise above to create a new version of the guessing game we made in day 8.
# This time the program should generate a random number, and you should tell the user whether their guess was too high,
# or too low, until they get the right number.

while True:
    guess = rn.randint(1,101)
    user_guess = int(input("enter a guess: ").strip())
    if user_guess == guess:
        print("you guesses correctly!")
        break
    elif user_guess>guess:
        print("too high")
        continue
    else:
        print("too low")