# Exercise
# Rewrite the following piece of code using a context manager:
        # f = open("hello_world.txt", "w")
        # f.write("Hello, World!")
        # f.close()

with open('hello_world.txt','w')as newFile:
    newFile.write('Hello, World!')

# Use append mode to write "How are you?" on the second line of the hello_world.txt file above.
with open('./hello_world.txt','a') as newFile:
    newFile.write('How are you?')

# Take the list of dictionaries we created from the Iris flower data set and write it to a new file in CSV format.


with open('./iris.csv','r') as iris_file:
    iris_data = iris_file.readlines()

irises = []
headers = iris_data[0].strip().split(',')
for item in iris_data[1:]:
     iris = item.strip().split(',')
     irises.append(dict(zip(headers,item))) # previously written code.

# converting the irises dictionary back into a csv file
with open('iris_data.csv','w') as new_iris:
    for iris in irises:
        new_iris.write(','.join(iris.values()+'\n'))
