# 1) Ask the user for an integer between 1 and 10 (inclusive). 
# If the number they give is outside of the specified range, raise a ValueError and inform them that their choice was invalid.
# user_input = int(input("input any integer between 1 and 10: "))
# try:
#     if user_input in range(1,11):
#         print(f"{user_input} is a valid integer in the range (1-10)")
# except user_input not in range(1,11):
#     raise ValueError("input is not a valid integer in the specified range")

# 2) Below you'll find a divide function. 
# Write exception handling so that we catch ZeroDivisionError exceptions, TypeError exceptions, and other kinds of ArithmeticError.

# def divide(a, b):
#     try:
#         print(a / b)
#     except ZeroDivisionError:
#         print("cannot divide by zero")
#     except TypeError:
#         raise TypeError("cannot perform division on strings") from None
# divide(9,0)
# divide(9,'a')


# 3) Below you'll find an itemgetter function that takes in a collection, and either a key or index. 
# Catch any instances of KeyError or IndexError, and write the exception to a file called log.txt, 
# along with the arguments that caused this issue. Once you have written to the log file, reraise the original exception.

def itemgetter(collection, identifier):
    # try:
    #     with open('log.txt','a') as logs:
    #         pass
    # except FileNotFoundError:
    #     with open('log.txt','x') as logs:
    #         pass
    try:
        return collection[identifier]
    except IndexError:
        raise IndexError(f"{identifier} is not a valid index")
    except KeyError:
        raise KeyError(f"{identifier} is not a valid key")
    
my_dict = {'name':'kofi','age':10,'color':'black'}    
itemgetter(my_dict,'er')