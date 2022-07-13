from functools import reduce

lis = [1,2,3,4,5]
num = reduce(lambda x,y:x*y,lis)
print(num)