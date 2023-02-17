# 1) Write a short guessing game program using a while loop.
# The user should be prompted to guess a number between 1 and 100, and you should tell them 
# whether their guess was too high or too low after each guess. 
# The loop should keeping running until the user guesses the number correctly.



initial_guess = 29
user_guess = int(input("enter a guess"))
while user_guess!=initial_guess:
    if user_guess > initial_guess:
        print("too high")
    else:
        print("too low")

    user_guess = int(input("enter a guess"))
print("correct guess")
      



# 2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
# Remember that strings are collections, and they are iterable, so you can iterate over the string, 
# which will yield one character at a time.

text =  'python'

for letter in list(text):
    if letter == 'o':
        continue
    print(letter)


# 3) Using one of the examples from earlier—or a solution entirely of your own—create 
# a program that prints out every prime number between 1 and 100.

# for numbers less than the curent number, divide the current number by em.

prime_list = []
for num in range(2,101):
    for divisor in range(2,num):
        if num%divisor == 0:
            break
    else:
        prime_list.append(num)

#show the list      
print(prime_list)
        