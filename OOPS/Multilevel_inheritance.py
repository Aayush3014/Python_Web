class Father:
    father_name = "Father"


class Son(Father):
    son_name = "son"


class Grandson(Son):
    grandson_name = "grandson"


# From Grandson class we can access all the above classes.
a = Grandson()
print(a.father_name)
print(a.son_name)
print(a.grandson_name)


# From Son class we can access only son and father class
b = Son()
print(b.father_name)
print(b.son_name)

# From Father class we can only access Father class
c = Father()
print(c.father_name)
