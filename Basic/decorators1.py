def div(a,b):       # a is numerator 
                    # b is denominator
    print(a/b)

# div(2,4)

# If we want numerator always be bigger than denominator without changing the existing function

# we will use decorators

def smart_div(func):   # func is function that will be passed as argument while compiling.
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div = smart_div(div)
div(2,4)