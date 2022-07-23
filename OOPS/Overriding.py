from tkinter import ON


class One:
    classvar1 = "I am a class variable of Class one."
    def __init__(self) -> None:
        self.var1 = "variable 1 of class One constructor."
        # self.classvar1 = "Instance variable of class One"
    
class Two(One):
    classvar1 = "I am a class variable of Class two."
    def __init__(self) -> None:
        super().__init__()
        self.var2 = "variable 2 of class two constructor."

a = One()
b = Two()
print(b.classvar1)