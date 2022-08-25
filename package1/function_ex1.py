def sumi_hakabai(n1):
    return (n1%10+n1//10%10+n1//100)

num=int(input('enter 3 digits number: '))
print(sumi_hakabai(num))
