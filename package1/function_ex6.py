def line (s,b):
    list1=[]
    for i in range(s,b+1):
        list1.append(i)
    return list1

# main
a=int(input('enter number: '))
c=int(input('enter a bigger number: '))
print(line(a,c))