# Loops
spam = 0
if spam < 5:
    print("Enter Name")
    spam += 1


spam = 0
while spam < 5:
    print("Enter Name")
    spam += 1


name = ''
while name != 'Your Name':
    print("Enter Your Name")
    name = input()
print("thank you")

# same code as above but using break statment
while True:
    print("Enter your Name")
    name = input()
    if name == 'Your Name':
        break
print("Thank you")

#
name = ''
while not name:
    print("Enter Your Name")
    name = input()
    print("How many guests")
    noGuest = int(input())
    if noGuest:
        print("All welcome")
print('done')

# For loops
for i in range(5):
    print("Ak gud work"+" ("+str(i)+") ")

#
sum = 0
for i in range(101):
    sum = sum + i;
print(sum)

# range
for i in range(10,20):
    print(i)

for i in range(10,20,2):
    print(i)

# Random Module
import random
for i in range(4):
    print(random.randint(1,15))

# System modeul
import sys

while True:
    print("Enter exit to exit from the program")
    response = input()
    if response == 'exit':
        sys.exit()
    print('Your response is '+response)

import random

print(random.randint(10,30))
print(random.random())
print(random.choice([1,2,5,6,7]))
print(random.sample(range(1,80),20))
print(random.uniform(0,1))

import math

print(math.ceil(3.2551)) # returns higher number
print(math.fabs(3.2551))
print(math.factorial(5)) # factorial of number
print(math.floor(3.268)) # returns lower number
print(math.fmod(2.4,2)) # returns reminder mod function
print(math.isnan(5))
print(math.log(100,10))
print(pow(2,5))

