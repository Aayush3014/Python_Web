# def fibonacci_iterative(n):
#     n1,n2 = 0,1
#     print(n1)
#     print(n2)
#     for i in range(n-2):
#         n3 = n1+n2
#         n1,n2 = n2,n3
#         print(n3)
# fibonacci_iterative(5)


def fibo_recursive(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)

a = int(input("Enter terms :  "))
for i in range(a):
    print(fibo_recursive(i))