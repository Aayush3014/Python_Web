import email
from tkinter.messagebox import NO


class Employee:
    def __init__(self, fname, lname) -> None:
        self.fname = fname
        self.lname = lname
        # self.email = unge

    def printdetails(self):
        return f"The Employee is {self.fname} {self.lname}"

    @property
    def email1(self):
        if self.fname == None or self.lname == None:
            return "Email is deleted"

        return f"{self.fname}.{self.lname}@google.com"

    # It will set the new value of email as given in line 26
    @email1.setter
    # and it will also change the value of fname and lname.
    def email1(self, string):

        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email1.deleter       # It is created to delete the value created by setter
                          # entities created by setter decorator cannot be deleted normally.
    def email1(self):
        self.fname = None  # we have to use deleter for deleting the value.
        self.lname = None


ayush = Employee("Ayush", "Kumar")
# print(ayush.printdetails())
# print(ayush.email1)
# ayush.fname = "Us"
# print(ayush.email1)
ayush.email1 = "this.that@codewithharrycom"
print(ayush.email1)
print(ayush.fname)
del ayush.email1
print(ayush.email1)