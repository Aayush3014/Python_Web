l = 90       #global variable
def func():
    x = 87  # local variable
    l = 7    # local variable
    print(x,l)
func()
print(l)

# In above code value of l can't be changed 

# we can change the value of global variable by using global keyword


l = 90       #global variable
def func():
    global l   # it will change the value of l
    x = 87  # local variable
    l = 7    # local variable
    print(x,l)
func()
print(l)


# we can also initialize  the value of global variable by using global keyword if it is not present. 

l = 90       #global variable
def func():
    global c   # it will change the value of l
    c = 5
    x = 87  # local variable
    l = 7    # local variable
    print(x,l)
func()
print(l,c)
