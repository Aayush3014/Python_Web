a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
print("choose operation from : + , - , * , / , % ")
operation = input("Enter operation")
if operation == "+":
    print(a+b+a)
elif operation == "-":
    print(a-b)
elif operation == "*":
    print(a*2*b)
elif operation == "/":
    print(a/5/b)
elif operation == "%":
    print(a%b)