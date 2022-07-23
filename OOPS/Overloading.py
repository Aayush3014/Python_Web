class Employee:
    no_of_leaves = 10

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


    def __add__(self,other):
        return self.salary + other.salary

harry = Employee("Harry",48655,"t")
rohan = Employee("Rohan",556455,"s")

print(harry + rohan)