y = input()
s = 0
while y[s+1]!="d":
  s += 1
number = int(y[:s+1])
side = int(y[s+2:])
if number == 1:
  number_summa = number * side
elif number > 1:
  number_summa = (number * side) - number + 1
print(str(int(100 / number_summa))+"%")