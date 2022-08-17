from random import randint

num=randint(0,1850)

if 100<=num<=999:
    print(num//100+num//10%10+num%10)
else:
    print('error')
