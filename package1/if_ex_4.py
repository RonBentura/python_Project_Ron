from random import randint

num1=randint(1,1000)
num2=randint(1,1000)
print(num1,num2)
#num1=int(input(':'))
#num2=int(input(':'))

if num1%2==0 and num2%2==0:
    print(num1+num2)
else:
    print(num1*num2)