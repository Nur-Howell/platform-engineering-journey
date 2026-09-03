"""

def add(a, b):
    result = a + b
    return result

print(add(3, 5))  # Output: 8

""" 
"""
a = 2
b = 3
if a > b:
    print("a is greater than b")
else:
    print("a is not greater than b")  # Output: a is not greater than b

"""

cars = ["Toyota", "Honda", "Ford"]
a = cars[0]
b = cars[1]
print(len(cars))  # Output: 3

length = len(cars)

try:
    for i in range(length):
        print(cars[i])  # Output: Toyota, Honda, Ford
except IndexError:
    print("Index out of range")