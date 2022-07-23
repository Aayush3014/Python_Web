# https://docs.python.org/3/library/operator.html
# link of funtions for overloading methods using dunder methods.



class Employee:
    no_of_leaves = 10

    def __init__(self, aname, asalary, arole):
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

    def __add__(self, other):                # Special dunder method created to overload add operator
        return self.salary + other.salary  # salary of both objects.

    def __truediv__(self, other):
        return self.salary / other.salary


# Print function will give priority to str function if both function are provided
# If only one is provided the calling str and repr will return only which function is overloaded.
# As given in below code.

    def __repr__(self):
        return f"Employee('{self.name}',{self.salary},'{self.role}')"

    def __str__(self) -> str:
        return f"name is {self.name}. Salary is {self.salary}.role is {self.role}"


harry = Employee("Harry", 45, "t")
# rohan = Employee("Rohan", 5, "s")

# print(harry + rohan)
# print(harry/rohan)
print(harry)
