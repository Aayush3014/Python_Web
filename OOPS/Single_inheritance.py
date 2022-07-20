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

class Programmer(Employee):
    def __init__(self, aname, asalary, arole,languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        
        # super().__init__(aname, asalary, arole)
        self.languages = languages
    def printprog(self):
        return f"name is {self.name}. Salary is {self.salary}.role is {self.role} and the languages is {self.languages}"        


harry = Employee("Harry",48655,"t")
rohan = Employee("Rohan",556455,"s")

karan = Programmer("Karan",8995,"p",["python","cpp"])
print(karan.printprog())