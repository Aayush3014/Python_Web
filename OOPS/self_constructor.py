class Employee:
    no_of_leaves = 8

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"name is {self.name}. Salary is {self.salary}.role is {self.role}"
    
harry = Employee("Harry",48655,"t")
rohan = Employee("Rohan",556455,"s")

# harry.name = "Harry"
# rohan.name = "Rohan"
# rohan.salary = 6564
# rohan.role = "Student"
print(rohan.printdetails())
print(harry.printdetails())