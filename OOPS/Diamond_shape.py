class A:
    def met(self):
        print("I am a method from class A")


class B(A):
    def met(self):
        print("I am a method from class B")


class C(A):
    def met(self):
        print("I am a method from class C")


class D(B,C):
    def met(self):
        print("I am a method from class D")


a = A()
b = B()
c = C()
d = D()

print(d.met())