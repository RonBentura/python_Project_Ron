def comp (n1,n2):
    if n1>n2:
        return (f'big {n1}  ') + (f'small {n2}')
    if n1<n2:
        return (f'big {n2}  ') + (f'small {n1}')

def line (s,b):
    list1=[]
    for i in range(s,b+1):
        list1.append(i)
    return list1


# main
a=int(input('enter number: '))
c = int(input('enter a bigger number: '))

print(comp(a,c))
if a>c:
    print(line(c,a))
if c>a:
    print(line(a,c))


