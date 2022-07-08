def recursion_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac*(i+1)
    return fac 


def recursion_recursive(n):
    if n == 1:        # BAse Case 
        return 1
    else:
        return n * recursion_recursive(n-1)   # Recursive case
print(recursion_iterative(5))
print(recursion_recursive(5))