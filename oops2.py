class Employee:
    no_of_leaves = 8
    pass
harry = Employee()
rohan = Employee()

harry.name = "Harry"
rohan.name = "Rohan"
print(Employee.no_of_leaves)
print(harry.no_of_leaves)
harry.no_of_leaves = 10
Employee.no_of_leaves = 20
print(harry.no_of_leaves)
print(Employee.no_of_leaves)