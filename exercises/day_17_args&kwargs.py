# 1) Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers.
# Remember that we can use the sum function to add the values in an iterable.

# answer
def adder(*args):
    return sum(args)

print(adder(1,5,4,8))

# 2) Create a function that accepts any number of positional and keyword arguments, and that prints them back to the user.
# Your output should indicate which values were provided as positional arguments, 
# and which were provided as keyword arguments.
def printer(*args,**kwargs):
    result = print(f"1. posiotional arguments{args}\n2. Keyword arguments{kwargs}")
    return result

printer(3,5,75,4,6,i=3,l=0,m=9)


# 3) Print the following dictionary using the format method and ** unpacking.

country = [{
"name": "Germany",
"population": "83 million",
"capital": "Berlin",
"currency": "Euro"
}]

template = """Name:{name}
Population: {population}
Capital: {capital}
Currency: {currency}"""

def pp(countries_list):
    for deet in countries_list:
        print(template.format(**deet))


pp(country)

# 4) Using * unpacking and range, print the numbers 1 to 20, separated by commas.
# You will have to provide an argument for print function's sep parameter for this exercise.

print(*range(1,21),sep=',')


# 5) Modify your code from exercise 4 so that each number prints on a different line.
# You can only use a single print call.
print(*range(1,21),sep=',')