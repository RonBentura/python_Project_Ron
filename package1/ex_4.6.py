list1=[1,2,3,4,5,6,7,8,9,10]

#a
print(list1[-3:])


print('================================================')
#b
print(list1[::-1])


print('================================================')
#c,d
for N in list1:
    if N%2!=0:
        print((N),end=' ')


print(f'\n')
print('================================================')
#e
print(f'\n')
list1=[1,2,3,4,5,6,7,8,9,10]
b=int(input('enter number: '))
b2=int(input('enter number: '))
list1=list1[:4]+[b]+[b2]+list1[6:]

b1=int(input('enter number: '))
list1+=[b1]
print(list1)

print('================================================')
#f
list1=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(list1)):
    list1[i]*=2

#g
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1[0],list1[-1]
print(list2)



