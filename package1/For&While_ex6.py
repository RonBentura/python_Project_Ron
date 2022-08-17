g=int(input('enter grade: '))
count=0
count1=0
s=0
s1=0
while 0<=g<=100:
    if g>=60:
        count+=1
        s+=g
        avr=s/count
        g = int(input('enter grade: '))
    elif g<60:
        count1+=1
        s1+=g
        avr1=s1/count1
        g = int(input('enter grade: '))
else:
    print(f'the failed test average is: {avr1}\nthe pass test average is: {avr}')




