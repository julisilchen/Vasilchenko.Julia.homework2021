a = input("Введите любое число больше 2: ")
b = int(a)
c = list(range(2, b + 1))
d = 0
e = 0
# c[e]-делители-индексы
while (c[e] * c[e]) < b:
    while len(c) - 1 > d:
        d += 1
        if c[d] % c[e] == 0:
            del c[d]
            d -= 1

    e += 1
    d = e

print(c)

