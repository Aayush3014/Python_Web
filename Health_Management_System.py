# Health management system
import datetime as d

def getdate():
    return d.datetime.now()


def entry(k):
    if k == 1:   # input for harry
        c = int(input("Enter the Choice\n1.Food\n2.Excercise\nEnter Choice : "))
        if c == 1:
            value = input("Enter Food\n")
            with open("HarryFood.txt","a") as har:
                har.write(str([str(getdate())])+": "+value+"\n")
      
      
        elif c == 2:
            value = input("Enter Exercise:\n")
            with open("HarryExercise.txt","a") as har:
                har.write(str([str(getdate())])+": "+value+"\n")
    

    if k == 2:   # input for rohan
        c = int(input("Enter the Choice\n1.Food\n2.Excercise\nEnter Choice : "))
        if c == 1:
            value = input("Enter Food\n")
            with open("rohanFood.txt","a") as har:
                har.write(str([str(getdate())])+": "+value+"\n")
      
      
        elif c == 2:
            value = input("Enter Exercise:\n")
            with open("rohanExercise.txt","a") as har:
                har.write(str([str(getdate())])+": "+value+"\n")


    if k == 3:   # input for hammad
        c = int(input("Enter the Choice\n1.Food\n2.Excercise\nEnter Choice : "))
        if c == 1:
            value = input("Enter Food\n")
            with open("HammadFood.txt","a") as har:
                har.write(str([str(getdate())])+": "+value+"\n")
      
      
        elif c == 2:
            value = input("Enter Exercise:\n")
            with open("HammadExercise.txt","a") as har:
                har.write(str([str(getdate())])+": "+value+"\n")


def retrieve(k):
    if k == 1:   # input for harry
        c = int(input("Enter the Choice\n1.Food\n2.Excercise"))
        if c == 1:
            with open("HarryFood.txt") as har:
                e = har.readlines()
                for i in e:
                    print(i,end=",")
      
      
        elif c == 2:
            with open("HarryExercise.txt") as har:
                e = har.readlines()
                for i in e:
                    print(i,end=",")

    if k == 2:   # input for rohan
        c = int(input("Enter the Choice\n1.Food\n2.Excercise"))
        if c == 1:
            with open("rohanFood.txt") as har:
                e = har.readlines()
                for i in e:
                    print(i,end=",")
      
      
        elif c == 2:
            with open("rohanExercise.txt") as har:
                e = har.readlines()
                for i in e:
                    print(i,end=",")


    if k == 3:   # input for hammad
        c = int(input("Enter the Choice\n1.Food\n2.Excercise"))
        if c == 1:
            with open("HammadFood.txt") as har:
                e = har.readlines()
                for i in e:
                    print(i)
      
      
        elif c == 2:
            with open("HammadExercise.txt") as har:
                e = har.readlines()
                for i in e:
                    print(i)


a = input("Enter choice to log or retrieve : ")
if a == "log":
    print("Enter Person Number To Enter data : \n1.Harry\n2.Rohan\n3.Hammad")
    input1 = int(input("Enter choice : "))
    entry(input1)
elif a=="retrieve":
    print("Enter Person Number To Enter data : \n1.Harry\n2.Rohan\n3.Hammad")
    input1 = int(input("Enter choice : "))
    retrieve(input1)