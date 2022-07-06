with open("filewrite2.txt") as f:
    a = f.readlines()
    print(a)

f = open("filewrite2.txt","r+")    #  "r+"" is for reading and writing.

print(f.readlines())
# f.write("you")
f.close()