# 1) Create an empty set and assign it to a variable.
new_set =set()
# 2) Add three items to your empty set using either several add calls, or a single call to update.
new_set.update(["kofi","ama","yaw"])
new_set.add("elvis")

# 3) Create a second set which includes at least one common element with the first set.
set2 = {"eva","melvin", "kofi", "zigi"}

# 4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.
#union
print(new_set.union(set2))
#symmetric_difference
print(new_set.symmetric_difference(set2)
)#intersection
print(new_set.intersection(set2))

# 5) Create a sequence of numbers using range, then ask the user to enter a number.
# Inform the user whether or not their number was within the range you specified.

numbers = range(17,29)

while True:
    guess = int(input("ener a number:\n>>> ").strip())
    if guess not in numbers:
        if guess < min(numbers):
            print("too low")
        elif guess> max(numbers):
            print("too high")
        print("try again")
        continue
    else:
        print("yay. you guessed the lucky number")
    break
