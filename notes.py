#day 1
#---------------------------
 # lists

# accessing items in a list
names = ["John", "Alice", "Sarah", "George"]
print(names[2])  # Sarah

# adding two lists
list1 = ["John", "Alice", "Sarah", "George"]
list2 = [1, 2, 4, 5]

list1 += list2
print(list1)    #['John', 'Alice', 'Sarah', 'George', 1, 2, 4, 5]

# appending items to a list
some_list = [10,'woman']
some_list.append('man')
print(some_list)    #[10, 'woman', 'man']

# inserting items to lists using indexes
number_list =  [1,2,4,5]
number_list.insert(2,3) #list_name.insert(index, item)
print(number_list)  #[1, 2, 3, 4, 5]

# removing items from a list
names = ["John", "Sarah", "Alice", "John"]
names.remove("John")
print(names)    #['Sarah', 'Alice', 'John']

# removing items when their value is unknown.
names = ["John", "Sarah", "Alice", "Mike"]
del names[0]
print(names)  # ['Sarah', 'Alice', 'Mike']

#clearing a list
names = ["John", "Sarah", "Alice", "John"]
names.clear()
print(names)    #[]


 # tuples
some_tuple =  ("aki","john","meyer")

# tuples are immutable. meaning we can't change them once they're definded.
# there's no .pop(), del, or .append() methods for tuples

 #tuples can be nested in a list
tuple_list = [("shrek", "animation",5),("DeadPool","action",10)
    ,("spiderman","action",9)]

 #Accessing values in nested collections
#syntax list[tuple_index][item_index]
#example:

print(tuple_list[0][1]) #animation

#---------------------------------------------------------------------------------------------#
#                                        # Day 2                                              #
#---------------------------------------------------------------------------------------------#
    
# Comparison operators
 #less than
print(5 < 10)     # True
 #greater than
print(3 > 10)     # False
print(8 > 8)    # False

 #upper and lower case of the same letter have different ascii values
print("B" < "b")  # True

print(25 > 25)   # False
print(25 >= 25)  # True

 #equality operator
print(0 == "0")                # False
print(0 == 0)                  # True
print(7 == 7.0)                # True
print("Hello" == "Hello!")     # False
print([1, 2, 3] == [1, 2, 3])  # True

 #not equal to operator
print(0 != "0")         # True
print(0 != 0)           # False
print("Hello" != "Hi")  # True

 #The `is` operator
 # this operator is used to check for exactness.
 # it checks for whether two items are exactly the same.
 # Not that they have the same values, but that they are exactly the same thing.
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) #false
 #this returns false because although the items in list a and b are equal, they're storeed in different memory addresses.
 # we can verify this by using the 'id' to check the location of each item.

print(id(a))  # 139806639351360
print(id(b))  # 139806638418944
 # we can clearly see the two items have different memory addreses implying they are not the same.

#  Conditional Statements
    # Conditional statements allow us to run some block on code if and only if some condition is met.
 #eg
age = int(input("How old are you? "))

if age < 18:
    print("Sorry, we can't serve you.")

#---------------------------------------------------------------------------------------------#
#                                        # Day 3                                              #
#---------------------------------------------------------------------------------------------#

    # FOR loops
# FOR loops allow us to repeat some action once for each item in a collection.

 # The break statement
# used to stop a loop at a certain criteria been met.
# not much note to add.


#---------------------------------------------------------------------------------------------#
#                                        # Day 4                                               #
#---------------------------------------------------------------------------------------------#
    #  FOR LOOPS

# for loops are great for two kinds of repeated actions:

# When we want to do something for each item in some group.
# When we want to do something a set number of times.
# syntax
# for some_condition:
#   do something

# Example
# let's write a loop to determine whether or not a number is prime.

dividend =  int(input("enter a number:\n"))

for divisor in range(2, dividend):
    if dividend%divisor == 0:
        print("not prime.")
        break
else:
    print(f"{dividend} is prime")




#---------------------------------------------------------------------------------------------#
#                                        # Day 5                                              #
#---------------------------------------------------------------------------------------------#

    # WHILE LOOP
# WHILE  loops are used :
# if we want to perform an action as many times as needed until some condition is met.
# if we want to perform some action over and over again forever.

#syntax
# While some_condition:
#   do something


# let's write a loop to determine whether or not a number is prime.

dividend =  int(input("enter a number:\n"))
divisor = 2

while dividend>divisor:
    if dividend%divisor ==0:
        print(f"{dividend} is not prime")
        break
    divisor += 1
else:
    print(f"{dividend} is prime")


#---------------------------------------------------------------------------------------------#
#                                        # Day 5                                              #
#---------------------------------------------------------------------------------------------#
    # Enumerate an Zip

movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]
for counter, (title, director, year) in enumerate(movies, start=1):
    print(f"{counter}. {title} ({year}), by {director}")

# The ZIP function is used to combine two or more iterables into one.
#syntax
# zip(iterable_1, iterable_2,....)
# eg:
# pet_owners = ["Paul", "Andrea", "Marta"]
# pets = ["Fluffy", "Bubbles", "Captain Catsworth"]
# results:
# ("Paul", "Fluffy"), ("Andrea", "Bubbles"), ("Marta", "Captain Catsworth")


