n=int(input('enter number: '))
count=0
while 0!=n:
    if n%3==0 or n%7==0:
        count+=1
    n = int(input('enter number: '))

print(count)
