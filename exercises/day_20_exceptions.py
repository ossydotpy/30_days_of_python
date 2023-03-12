# 1) Create a short program that prompts the user for a list of grades separated by commas.
# Split the string into individual grades and use a list comprehension to convert each string to an integer.
# You should use a try statement to inform the user when the values they entered cannot be converted.

# answer
def scorer():
    user_input = input("Enter a list of grades separated by commas: ").strip().split(",")
    try:
        grades = [int(grade) for grade in user_input]
        return grades
    except ValueError:
        print('cannot convert this object type!')

scorer()

# 2) Investigate what happens when there is a return statement in both the try clause and finally clause of a try statement.
def investigation():
    try:
        return 'from try'
    finally:
        return 'lol'
investigation()
#observation:
    #only the return statement from the finally block was triggered.


# 3) Imagine you have a file named data.txt with this content:
# There is some data here!

# Open it for reading using Python, but make sure to use a try block to catch an exception that arises if the file doesn't exist.
#     Once you've verified your solution works with an actual file, delete the file and see if your try block is able to handle it.

# When files don't exist when you try to open them, the exception raised is FileNotFoundError.

#answer
try:
    with open('data.txt','r') as book:
        content = book.readlines()
except FileNotFoundError:
    print('file doesnt exist')
