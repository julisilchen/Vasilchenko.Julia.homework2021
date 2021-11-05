from random import randint
import math
a = input("Введите количество чисел: ")
b = int(a)
num = []
for i in range(b):
  num.append(randint(0,100))
print(num)
