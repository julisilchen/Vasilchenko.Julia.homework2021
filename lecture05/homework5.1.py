x= open('taskk.txt','r')
y=x.readlines()
def slozhno(y):
  for num1 in y:
    for num2 in y:
      if int(num1)+int(num2)<2020:
        for num3 in y:
          if int(num1)+int(num2)+int(num3)==2020:
            print(num1, num2, num3)
            return (int(num1)*int(num2)*int(num3))
z=slozhno(y)
print(z)
z=str(z)
new_x = open('output1.txt', 'w')
new_x.write(z)
x.close()
new_x.close()