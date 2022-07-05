# seek() and tell() 

f = open("filewrite2.txt")
print(f.tell())              # tells us the position of pointer
print(f.readline())
f.seek(10)                   # it resets the positon of pointer
print(f.tell())
print(f.readline())
print(f.tell())
