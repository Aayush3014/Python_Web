# l = ["9","7","6","3"]
# a = list(map(int,l))
# print(a)

# def sq(a):
#     return a*a

# num = [4,5,7,8,9,6,2]


# square = list(map(sq,num))
# print(square)


# square = list(map(lambda x: x*x,num))
# print(square)

# Revisit

def square(a):
    return a*a
def cube(a):
    return a*a*a
func = [square,cube]
# num = [4,5,7,8,9,6,2]
for i in range(5):
    val = list(map(lambda x:x(i),func))
    print(val)