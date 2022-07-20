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


harry = Employee("Harry",48655,"t")
rohan = Employee("Rohan",556455,"s")

# harry.name = "Harry"
# rohan.name = "Rohan"
# rohan.salary = 6564
# rohan.role = "Student"
# print(rohan.printdetails())
# print(harry.printdetails())

print(Employee.info_leaves())