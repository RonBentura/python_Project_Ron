from random import randint
list1=[]
#a
for i in range(10):
    a=randint(0,100)
    list1.append(a)
print(list1)
#b
t1=tuple(list1)
print(t1)
#c
n=int(input('enter number: '))
t1+=(n,)
print(t1)
#d
list1=list(t1)
print(list1)
list2=list1[0:4]
list2+=list1[-4:]
t2=tuple(list2)
print(t2)

list2=list(t2)
list2.pop(0)
t2=tuple(list2)
print(t2)
