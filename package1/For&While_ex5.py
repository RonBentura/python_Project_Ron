g=int(input('enter grade: '))
count=0
s=0
while 0<=g<=100:
    if g>=60:
        count+=1
        s+=g
    avr=s/count
    g = int(input('enter grade: '))
else:
    print(f'the average is: {avr}')

