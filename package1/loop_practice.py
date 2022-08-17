G=int(input('enter grade: '))

while G>100 or G<1:
    print('invalid grade , try again')
    G = int(input('enter grade: '))

if G>70:
    print('passed')
if G<70:
    print('failed')

