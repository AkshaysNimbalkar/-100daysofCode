# lists and tuples used for sequntial data
# sets for unorderd unique values

courses = ['history', 'Marathi', 'Hindi', 'Sanskrit']
courses.append('English')
#courses.insert(0,'Java')
#len(courses)
courses2 = ['French', 'spanish']
courses.insert(0,courses2)
print(courses[0])
courses3 = ['Latin', 'Arab']
courses.extend(courses3) #extend add multiple values to list one by one
print(courses)

courses.remove('Java')
print(courses)

courses.remove(courses[0])

#courses.sort()

sorted_courses = sorted(courses)
print(sorted_courses)

sorted_courses.index('Hindi')

for index,course in enumerate(courses, start=1):
    print(index,course)

courses_str = " - ".join(courses)
type(courses_str)
print(courses_str)

new_courses = courses_str.split(' - ')
type(new_courses)
print(new_courses)

# lists are mutable : if want to change or mody values use lists
list1 = ['A', 'B', 'C', 'D', 'E']
list2 = list1
list1[0] = 'Z' ## values are changing mutable

print(list1)
print(list2)

# tuples are Im-mutable: i.e we cant use remove, update, modify methods:
tuple1 = ('A', 'B', 'C', 'D', 'E')
tuple2 = tuple1
tuple1[0] = 'Z' # Error

print(tuple1)
print(tuple2)

# Sets are unique not duplicate values {}
set1 = {1,2,3,4,5,6,7,2,3}
type(set1)
print(set1)

set2 = {11,12,3,14,5,15,6}

set1.intersection(set2)
set1.union(set2)
set1.difference(set2) #prasent set1 but not in set2

# empty list
list1 = []
list1 = list()

# empty tuple
tuple1 = ()
type(tuple1)
type1 = tuple()

# empty sets
set1 = {}
type(set1) #dictionary

set1 = set()
type(set1)

###################################   Slicing   ###################################

#list = [start:end:step]

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
list1[0:9]
list1[4:8]
list1[4:-2]
list1[-2:-5:-1]
list1[::-1]

url = "https://www.google.com"
url[0:8]
url[-3:]
url[-10:-4]

#########################3 Sorting Lists, tuples, dicts ############

li = [2,3,4,2,1,8,75,25,1,56,2,4,8]

s_li = sorted(li, reverse=True)
print("Sorted", s_li)

li.sort(reverse=True)
print("original", li)

tup = (2,5,4,2,9,8,7)
tup_sort = tup.sort() # tuple doesn't have sort method

tup = sorted(tup)
print(tup)

dict = {'name':'Akshay', 'job' : 'data scientist', 'age':None, 'os':'win'}
dict.sort() # also dont have sort method

sor_dict = sorted(dict)
print(sor_dict)


from operator import attrgetter

class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.first, self.last, self.salary)



e1 = Employee('Akshay', 'Nimbalkar', 50000)
e2 = Employee('Monika', 'Jadhav', 60000)
e3 = Employee('Kalyani', 'Mitragotri', 70000)

Employee = [e1, e2, e3]


##   return emp.name
# s_employee = sorted(employee) # so we need keys in order to sort this so write custom fuction to sort this
#s_employee = sorted(employee, key=lambda e in e.name)
s_employee = sorted(Employee, key=attrgetter('name'))
