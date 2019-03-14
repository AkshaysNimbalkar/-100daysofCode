def getNumber(number):
    if number == 1:
        return 'Number generated is One'
    elif number == 2:
        return 'Number generated is Two'
    elif number == 3:
        return 'Number generated is Three'
    elif number == 4:
        return 'Number generated is Four'
    elif number == 5:
        return 'Number generated is Five'
    elif number == 6:
        return 'Number generated is Six'
    elif number == 7:
        return 'Number generated is Seven'
    elif number == 8:
        return 'Number generated is Eight'
    elif number == 9:
        return 'Number generated is Nine'

import random as rand
number = rand.randint(1,10)
fortune = getNumber(number)
print(fortune)

print(getNumber(rand.randint(1,9)))

print("Start")
print("End")

# to avoid new line generation will use
print("start", end="")
print("End")


print("start", "End")
print("start", "end", sep=",")


def spam():
    global eggs # tells function that this is global varibale no need to create local variable
    eggs = "spam"

eggs = 'global'
spam()
print(eggs)

### Error handling ###

def spam(divisor, dividor):
    try:
        return divisor / dividor
    except ZeroDivisionError:
        print('Error: Invalid argument')

spam(5,2)
spam(5,0)



def spam(dividor):
    return 45/dividor
try:
    print(spam(5))
    print(spam(10))
    print(spam(0))
    print(spam(3)) # not excuted becox control moves from zero to except and after that controler excites statements after except block
except ZeroDivisionError:
    print("Error : invalid argument")


# guess the number:

import random

secreate_number = random.randint(1,20)
print("I am thinking about number betwee 1 to 20")

def guessthNumber(user_num):
    for i in range(1, 7):
        if user_num < secreate_number:
            return print("Yor are thinking Too low", user_num)
        elif user_num > secreate_number:
            return print("yor are thinking too high", user_num)
        else:
            return print("You are correct", user_num)


user_num = input("Guess number between 1 to 20")
user_num = int(user_num)

guessthNumber(user_num)



def collatz(num):
    if num % 2 == 0:
        return print(num // 2)
    else:
        return print(3 * num + 1)

number = input("Enter Integer number")
try:
    number = int(number)
except:
    print("Please enter valid integer")

collatz(number)


