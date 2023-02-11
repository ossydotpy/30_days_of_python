# Exercises
 # 1. Try to approximate the behaviour of the `is` operator using `==`.
 # Remember we have the `id` function for finding the memory address for a given value,
 # and we can compare memory addresses to check for identity.


#1. approximate the behaviour of the `is` operator using `==`

def isoperator(var1,var2):
    id1 = id(var1)
    id2 = id(var2)
    if id1==id2:
        print(True)
    else:
        print(False)

x = [1,3,4]
y = [1,3,4]
isoperator(x,y) #False

# 2. Try to use the is operator or the id function to investigate the difference between this:
 # `numbers = [1, 2, 3, 4]`
 # `new_numbers = numbers + [5]`
 # And this:
 # `numbers = [1, 2, 3, 4]`
 # `numbers.append(5)`
 #  Are new_numbers and numbers the same thing? What about numbers before and after we append 5?

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
numbers = [1, 2, 3, 4]
numbers.append(5)


numbers == new_numbers  #True
numbers is new_numbers  #False
id(new_numbers) is id(numbers)  #False
id(new_numbers) == id(numbers)  #False
#results show that the two lists are similar but not the same since they're stored in dofferent locations


  #  3) Ask the user to enter a number.
  #  Tell the user whether the number is positive, negative, or zero.

number =  input("\nPlease input a number:\n")
if number//2==0:
    print("{number} is an even number")
elif number//2 ==1:
    print("{number} is and odd number")
elif number == 0:
    print("you entered Zero")
else:
    print("please input a an positive whole number")



#  4) Write a program to determine whether an employee is owed any overtime.
 #  You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.
 #  If the employee worked more than 40 hours,
 #  you should print a message which says the employee is due some additional pay,
 #  as well as the amount due. The additional amount owed is 10% of the employees hourly wage 
 #  for each hour worked over the 40 hours. 
 #  In effect, the employees get paid 110% of their hourly wage for any overtime.

hourly_wage = int(input("what is your hourly wage?:\n"))
hours_worked = int(input("how many hours have you worked this week?:\n"))
overtime = hours_worked - 40
amount_due = ((10/100)*hourly_wage)*overtime

if hours_worked>40:
    print(f"Payment due: ${amount_due}")
else:
    print("you are not owed any payment")
