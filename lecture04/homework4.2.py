from random import randint
import math
a = input("Введите количество чисел: ")
b = int(a)
num = []
for c in range(b):
  num.append(randint(0,100))
print(num)

for c in range(b-1):
for d in range(b-c-1):
    if num[d]>num[d+1]:
      num[d], num[d+1]= num[d+1], num[d]

print(num)