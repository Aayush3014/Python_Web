# Public , Protected , Private
class Employee:

    no_of_leaves = 10
    _protec = 52
    __private = 96


    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):   # Instance Methods
        return f"name is {self.name}. Salary is {self.salary}.role is {self.role}"

    @classmethod
    def info_leaves(cls):
        return cls.no_of_leaves


    @staticmethod
    def info():
        print("hellooooooooo")

class Employee2(Employee):
    pass


harry = Employee("Harry",48655,"t")
rohan = Employee("Rohan",556455,"s")

emp = Employee("emp",65655,"k")

emp2 = Employee2("emp2",8556,"5")

# print(emp.no_of_leaves)   # Accessing Public Variable

# print(emp._protec)        # Accessing Protected Variable

# print(emp._Employee__private)      # Accessing Private Variable


"""Accessing variables form derived Class"""

# print(emp2.no_of_leaves)   # Accessing Public Variable

# print(emp2._protec)        # Accessing Protected Variable

# print(emp2._Employee2__private)      # Accessing Private variable 
#                                     # Here We cannot access Private variable from derived CLass