def shalosh(Q):
    if 99<Q<1000:
        return True
    else:
        return False
#main
num=int(input('enter 3 digits number: '))
if shalosh(num) is True:
    print('valid')
else:
    print('invalid')

