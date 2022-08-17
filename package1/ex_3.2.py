n = int(input('enter number: '))

for i in range(2,n):
    if n%i==0:
        print('dont rishoni')
        break
else:
    print('rishoni')
