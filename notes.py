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