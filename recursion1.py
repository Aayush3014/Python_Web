def recursion_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac 
def recursion_recursive(n):
    if n == 1:
        return 1
    else:
        return n * recursion_recursive(n-1)
print(recursion_iterative(5))
print(recursion_recursive(5))