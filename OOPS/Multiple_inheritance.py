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


class Player:
    no_of_games = 4
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def printPlayer(self):
        return f"The name is {self.name} and game is {self.game}"

# class CoolProg(Employee,Player):
#     pass

class CoolProg(Player,Employee):
    pass

harry = Employee("Harry",48655,"t")
rohan = Employee("Rohan",556455,"s")

karan = CoolProg("karan",["prog","player"])
print(karan.printPlayer())