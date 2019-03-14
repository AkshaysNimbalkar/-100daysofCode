spam = [0, 1, 5, 6]
spam[2]

spam = [[2, 5], 7, 8]
spam[0]
spam[0][1]

# slicing: we can access multiple elements of list
spam = ['cat', 'bat', 'rat', 'elephant']
spam[-1]
spam[-4]
spam[0:4]
spam[1:3]
spam[1:-1]
spam[:2]
spam[1:]
spam[:]

del spam[2]
spam

del spam['bat'] # u cant delete as list indices are only int not strings

# write a program to accept catnames as input
catNames = []

while True:
    print("Enter the name of cat" + str(len(catNames) + 1) + " or enter to stop")
    name = input()
    if name == " ":
        break
    else:
        catNames = catNames + [name]

print("cat names are: ")
for name in catNames:
    print(name)

# for loop on list
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + 'in supplies is: ' + supplies[i])


# not in

def getPets(name):

    if name not in myPets:
        return print("Your pet is not prasent"+ name)
    else:
        return print("Take you pet" + name)


myPets = ['Zophie', 'Pooka', 'Fat-tail']
name = input("Enter you pet name")
getPets(name)

# multiple assignments
a, b = 'Akshay' , 'Sama'
b, a = a, b
b, a

# Augmented assignment operator
spam = 42
spam += 1
print(spam)

# list have ondex method if that vale is prasent in list it will return index els eretun erroe
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
supplies.index('pens')
supplies.index('blinders')
supplies.index('binders')

# Insert() and append() method to add element in list: o0n;y these methods are for list
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
supplies.append('chock')
supplies # add at the end

supplies.insert(3,'Board')
supplies

supplies.remove('chock') # if the value appears in multiple times only first occurance will be delteted

supplies.sort()
supplies

supplies.sort(reverse=True)
supplies

spam = ['a', 'A', 'z', 'Z']

spam.sort()
spam

spam.sort(key=str.lower)
spam

import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages)-1)])

name = "Samapti"
name[5]
name[-1]
name[2:4]
name[:-4]
'a' in name

for i in name:
    print(i)

name[5] = 'k' # immutable

## Tuples: tuples are same like list but only difference is written in  ( ) and
# tuples are immutable like strings

eggs = ('hello', 42, 0.5)
eggs[0]
eggs[0:2]

# Tuples cannot have their values modified, appended, or removed
eggs[1] = 27 # type error

type(('hello',)) # trailing comma tells it is tuple
type(('hello'))

# use tuples when you want orderd sequence of values that never never changes.

eggs = ["hello", 42, 0.5]
milk = eggs

milk[2] = "Ak"

eggs

# to avoid this referencing uodate use copy() and DeepCopy()
import copy
spam = ['a', 'b', 'c', 'd', 'e']
cheese = copy.copy(spam)
cheese[1] = 42
spam
cheese


spam = ['apples', 'bananas', 'tofu', 'cats']


def getList(spam):
    return ",".join(spam)

getList(spam)


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


# output
#   ..OO.OO..
#   .OOOOOOO.
#   .OOOOOOO.
#   ..OOOOO..
#   ...OOO...
#   ....O....