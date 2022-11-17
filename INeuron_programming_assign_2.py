#1.write a program to convert kilometres to miles?

#Ans)
km=int(input())
miles=km/1.60934
print('For {}km distance when converted to miles is {}'.format(km,miles) )


#2. Write a pyhton program to convert celcius to farenheit
#ans)
c=int(input('enter the temp in celcius'))

f=c*(9/5)+32

print("For celcius ={} equivalent farenheit={}".format(c,f))

# #3)write a pyhton program to dispaly calender?
# #ans)
import calendar

year =int(input('enter the year'))
month =int(input('enter month'))
print(calendar.month(year, month))
print(calendar.calendar(year))

#4) write a program to solve a qaudratic equation
#Ans)
import math
print("enter qaudratic coefficient of a quadratic equation")
a=int(input('enter coeff of a:'))
b=int(input('enter coeff of b:'))
c=int(input('enter coeff of c:'))

d=(b**2)-(4*a*c)

ans1= ((-1*b)+(math.sqrt(d)))/(2*a)
ans2=((-1*b)-(math.sqrt(d)))/(2*a)

#5)swap 2 varibale without  temp variable

a=90
b=50

c=a+b
a=c-a
b=c-b

print(' the value of a',a)
print('the value of b',b)

# print(ans1,ans2)
