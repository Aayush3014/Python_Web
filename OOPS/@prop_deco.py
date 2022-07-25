class Employee:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
        # self.email = unge

    def printdetails(self):
        return f"The Employee is {self.fname} {self.lname}"

    @property
    def email1(self):
        return f"{self.fname}.{self.lname}@google.com"


ayush = Employee("Ayush", "Kumar")
# print(ayush.printdetails())
print(ayush.email1)
ayush.fname = "Us"
print(ayush.email1)
