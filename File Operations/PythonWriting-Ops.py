# file writing

# f = open("filewrite2.txt","w")
# a = f.write("Ayush is a good boy Ayush is a bad boy\n") # storing the number of characters written in the file.
# # f.write("Ayush is a bad boy\n")
# print(a)
# f.close()

# Appending in a file

# f1 = open("filewrite3.txt","a")
# f1.write("Ayush is a good boy\n")
# f1.write("Ayush is a bad boy")
# f1.close()

# file writing and reading at same time

f = open("filewrite2.txt","r+")

print(f.readlines())
f.write("you")
f.close()