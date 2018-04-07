import math
print("Введите a,b,с для уравнения: ax^2+bx+c")
a=float(input("Введите a:"))
b=float(input("Введите b:"))
c=float(input("Введите c:"))
print('Уравнение имеет вид:',a,'x^2+',b,'x','+',c)
d=b*b-4*a*c
if d<0:
   print("Решений нет")
else:
   x1=(-b+math.sqrt(d))/(2*a)
   x2=(-b-math.sqrt(d))/(2*a)
   print("Ответ:")
   print("x1=",x1)
   print("x2=",x2)
print('Конец!')
