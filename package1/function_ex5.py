def sumo(n1):
    list1=[]
    for i in range(1,n1+1):
        list1.append(i)
    return sum(list1)

#main
for n in range(5):
    a=int(input('enter number: '))
    print(sumo(a))


