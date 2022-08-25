from random import randint

list1=[]
for i in range(10):
    num=(randint(0,100))
    list1.append(num)

print(list1)

for item in range(len(list1)):
    list1[item]*=2

print(list1)



print(list1[2:8])
print(list1[-3::])
print(list1[-3::-1])
print(list1[:7])





