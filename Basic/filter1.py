lis = [1,2,3,4,5,6,7,8,9]
def greater_5(num):
    return num>5

greater_num_5 = list(filter(greater_5,lis))
print(greater_num_5)