a = input("Введите первое число : ")
b = input("Введите второе число : ")
c1 = int(a)
c2 = int(b)
if c1 < c2:
    c1 = int(b)
    c2 = int(a)
d = c1 % c2
e = c1 // c2
d0 = c2

while d != 0:
    d0 = d
    d = c2 % d
print(d0)