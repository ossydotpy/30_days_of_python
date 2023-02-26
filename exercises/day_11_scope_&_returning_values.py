# 1) Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power to raise
# the base to. The function should return the result of this operation.
# Remember we can perform exponentiation using the ** operator.

def exponentiate(base,power):
    return base ** power



# 2) Define a process_string function which takes in a string and returns a new string which has been converted to lowercase,
# and has had any excess whitespace removed.

def process_string(text):
    text = text.strip().lower()
    return text

# 3) Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary.
# The data should be in the following format:

# ("Tom Hardy", "English", 42)  # name, nationality, age
# You can choose whatever key names you like for the dictionary.

def actor_info(actor_tuple):
    actor_name, language, age = actor_tuple
    return f"({actor_name, {language}, {age}})"
    

# 4) Write a function that takes in a single number and returns True or False depending on whether or not the number is
# prime. If you need a refresher on how to calculate if a number is prime, we show one method in day 8 of the series.

def isPrime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
