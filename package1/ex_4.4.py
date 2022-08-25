list1=[]
for i in range(7):
    num=int(input('enter number: '))
    list1.append(num)
print(list1)

list2=[]
for i in range(7):
    num1=int(input('enter number: '))
    list2.append(num1)
print(list2)

list1+=list2

print(list1)

print(len(list1))

