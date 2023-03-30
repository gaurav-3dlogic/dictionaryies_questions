# Python program to find the sum of all items in a dictionary
a = {"Gaurav":100,"saini":200,"python":500,"java":100}

sum = 0

for key,value in a.items():
    sum += value
print(sum)
    