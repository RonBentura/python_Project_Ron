N1=int(input('enter number: '))
N2=int(input('enter number: '))
N3=int(input('enter number: '))

if N1 > (N2+N3)/2:
    print(N1)
elif N2 > (N1+N3)/2:
    print(N2)
elif N3 > (N1+N2)/2:
    print(N3)
else:
    print('invalid')
