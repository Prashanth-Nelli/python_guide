# Python Basics
# Author N.Prashanth Kumar.

# # ===== Variables Declaration ===== ##

name = "Nelli.Prashanth kumar"  # String
lastname = firstname = ''
age = 20  # integer
salary = 30000.00  # float
expenses = 20000L  # Long
working_days = ("Mon", "Tue", "Wed", "Thu", "Fri")  # Tuple
known_languages = ["C", "Java", "Javascript", "Python"]  # List
friends = {
           'childhood_friends':[    {"name":"Sandeep Kumar", age:24},
                                    {"name":"Kiran", age:24}
                                ],
           "colleague's":[
                            {"name":"Balu", age:25},
                            {"name":"Venky", age:24}
                        ]
           }  # Dictionary


# # ===== Control Statements ===== #

# if Statement Start

if name:
    print name

# if else

if name and salary > 45000:
    print name + " is earning good amount of money"
else :
    print name + " is earning decent salary"    
        
# else if ladder  
    
if name and lastname:
    print lastname + " " + name
elif name and firstname:
        print name + " " + firstname

# # ===== Loops ===== ##

# While Loop

listlen = len(known_languages)
i = 0

while i < listlen:
    print known_languages[i]
    i += 1

# For Loop

for day in working_days:
    print day

for lang in known_languages:
    print lang
    
# # ===== Functions ===== ##

def log(text):
    print text

log("Hi Mr. Prashanth Kumar")

def sum(operand_1, operand_2):
    return int(operand_1) + int(operand_2)

log(sum(1, 2))

# # ===== Classes and Objects ===== ##

class Employee:  # Class Declaration
    "This Class is about an Employee Details"
    def __init__(self, name, age, salary, village):
        self.name = name
        self.age = age
        self.salary = salary
        self.village = village
    
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getVillage(self):
        return self.vilage
    def printDetails(self):
        print "Name:- " + self.name
        print "Age:- " + str(self.age)
        print "Village:-" + self.village
        
emp_1 = Employee("Nelli.Prashanth Kumar", 23, 30000, "Huzurabad")  # Object Initialization

emp_1.printDetails()



