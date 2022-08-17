N1=int(input('enter number 1:  '))
N2=int(input('enter number 2:  '))

while N1%2==0 and N2%2==0:
    if N1%2==0 and N2%2==0:
        print(N1+N2)
    N1 = int(input('enter number 1:  '))
    N2 = int(input('enter number 2:  '))
print(N1*N2)