# 1) Use map to call the strip method on each string in the following list:
humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",  
    "    Couldn't put Humpty together again."
]
def strip(args):
    return args.strip()

processed = map(strip,humpty_dumpty)
    # or
processed_list = map(lambda args:args.strip(),humpty_dumpty)

# Print the lines of the nursery rhyme on different lines in the console.
print(*processed, sep='\n')
print(*processed_list, sep='\n')
# Remember that you can use the operator module and the methodcaller function instead of a lambda expression if you want to.

# 2) Below you'll find a tuple containing several names:

names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")

# Use a list comprehension with a filtering condition so that only names with fewer than 8 characters end up in the new list.
# Make sure that every name in the new list is in title case.
new_names = [ele.title() for ele in names if len(ele)<8]
print(new_names)

# 3) Use filter to remove all negative numbers from the following range: range(-5, 11).
# Print the remaining numbers to the console.

print(*filter(lambda num:num<0,range(-5,11)))
