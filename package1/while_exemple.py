count=0
g=int(input('enter grade: '))

while 0<=g<=100:
    count+=1
    if g>70:
        print('pass')
    elif g<70:
        print('failed')
    if count==5:
        break
    g = int(input('enter grade: '))

else:
    print('invalid grade')