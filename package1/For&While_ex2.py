count=0
sum1=0
for i in range (6):
    num=int(input('enter number: '))
    if num%2==0:
        count=count+1
        sum1=sum1+num

avr=sum1/count
print(f'the sum is {sum1} \nthe average is {avr} ')