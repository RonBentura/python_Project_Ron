n=int(input('enter number: '))

while 10<=n<=99:
    if n%10==7 or n%7==0:
        print(f'lucky number is: {n}')
    n = int(input('enter number: '))

print('you are out of luck')