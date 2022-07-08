def print_num(normal,*args,**kw):
    print(normal)
    for i in args:
        print(i)
    for key,value in kw.items():
        print(f"{key} {value}")



k = {"1":"3","2":"4","8":"9"}
n = 23
lst = [4,"8",9,80]
print_num(n,*lst,**k)
