D=int(input('please enter day: '))
M=int(input('please enter month: '))
Y=int(input('please enter year: '))

if 1<=D<=31 and 1<=M<=12 and 1950<=Y<=2020:
    print(f'{D}/{M}/{Y%100}')
else:
    if D<1 or D>31:
        print('invalid day')
    if M<1 or M>12:
        print('invalid month')
    if Y<1950 or Y>2020:
        print('invalid year')








