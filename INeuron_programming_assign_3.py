#1)write a program to check if a number is positive ,negative or zero?
#Ans)
num=int(input())

if(num>0):
    print('number is positive')
elif(num<0):
    print('number is negative')
else:
    print("number is zero")

#2) check if a number is odd or even
#ans)

n=int(input('enter the number'))
if n%2==0:
    print(n,':the number is even')
else:
    print(n,':the number is false')

#write a program to check leap year
#ans)
n=int(input('enter year'))
if (n%400==0):
    print(n,'leap year')
elif( n%4==0 and n%100!=0):
    print(n,'leap year')
else:
    print('not leap')

#4)wite a program to check prime number

n=int(input('enter a number'))
if n>1:
    for i in range(2,n):
        if (n%i==0):
            print(n,'the number is not prime')
            break
    else:
        print(n,'is prime number')
else:
    print('not a prime')

#5)write a program to print all prime numbers n an interval 1-10000?
#ans)
for num in range (1,100):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
            print(num)
