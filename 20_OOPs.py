# class is a template used to create an object
#  Objects are instances of a class.


class Employee: #Class Definition
    def __init__(self,name,salary): 
        # Constructor (__init__)
        self.name = name    # Instance variable
        self.salary = salary    # Instance variable
        # __init__ is a constructor method
        # It automatically runs when a new object of the class is created.
         # 'self' represents the instance (object) of the class.
         # 'self' is the first parameter of instance methods in Python classes.
        # It refers to the current object (instance) of the class.
        # It is not a keyword, but by convention, we always name it 'self'.
        
    
    # Method (getSalary)
    def getSalary(self):
       return self.salary
    
Omm = Employee("Omm","10,000")     
# Creating Objects
print(Omm.salary)
print(Omm.name)
Omm.getSalary()

Isha = Employee("Isha","50,000")
# Creating Objects
print(Isha.salary)
print(Isha.name)
Isha.getSalary()