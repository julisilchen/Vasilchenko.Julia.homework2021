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

********************************************************************************
import random


# Сортирует массив a [0..n-1], используя сортировку Bogo
def bogoSort(x):
    a = len(x)
    while (is_sorted(x) == False):
        shuffle(x)


# Проверить, отсортирован ли массив или нет
def is_sorted(x):
    a = len(x)
    for c in range(0, a - 1):
        if (x[c] > x[c + 1]):
            return False
    return True


# Для генерации перестановки массива
def shuffle(x):
    a = len(x)
    for i in range(0, a):
        r = random.randint(0, a - 1)
        x[i], x[r] = x[r], x[i]


# Код драйвера для проверки выше
x = [3, 2, 4, 1, 0, 5]
bogoSort(x)
print("Sorted array :")
for c in range(len(x)):
    print("%d" % x[c]),