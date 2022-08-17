N=int(input('enter number: '))

while 100<=N<=999:
    print(N%10+N//100+N//10%10)
    N = int(input('enter number: '))
    if N<100 or N>999:
        print('end')