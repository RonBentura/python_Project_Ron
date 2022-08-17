g=int(input('enter grade: '))
count=0
count1=0
s=0
s1=0
while 0<=g<=100:
    if g>=60:
        count+=1
        s+=g
        avr = s / count
        if count < 1:
            avr == 0
        g = int(input('enter grade: '))
    elif g<60:
        count1+=1
        s1+=g
        avr1 = s1 / count1
        if count1 < 1:
            avr1 == 0
        g = int(input('enter grade: '))
else:
    print(f'the failed test average is: {avr1}\nthe pass test average is: {avr}')