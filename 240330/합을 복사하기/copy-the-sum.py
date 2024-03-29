a = 1
b = 2
c = 3

t = a
t2 = b
a = a + b+ c
b = t + b + c
c = t + t2 + c

print(a, b, c)