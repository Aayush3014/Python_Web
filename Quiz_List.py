# Both are correct


# l = [1,"a",5,"l",True,False]
# for i in l:
#     if type(i)==int:
#         print(i)
#     else:
#         pass

l = [1,"a",5,"l",True,False]
for i in l:
    if str(i).isnumeric():
        print(i)
    else:
        pass

