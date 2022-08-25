list1=[10,20,30,40,"hello",1,2,3]
#      0  1  2  3   4      5 6 7

print(list1)
print("list1[1]",list1[1])

list1[0]+=list1[2]
print("list1[0]+=list1[2]")
print(list1)

list1.append(100)
print("list1.append(100)")
print(list1)

list1+=[1,2,3]
print("list1+=[1,2,3]")
print(list1)

list1+=[44]
print("list1+=[44]")
print(list1)

list1*=2
print("list1*=2")
print(list1)

print("list1.index('hello')",list1.index("hello"))

print("list1.index('hello', 5)",list1.index("hello", 5))

print("list1.count(100)", list1.count(100))
print("list1.count(40)", list1.count(40))

list1.remove(1)
print("list1.remove(1)")
print(list1)

list1.remove("hello")
print("list1.remove('hello')")
print(list1)

list1=[10,20,30,40,"hello",1,2,3]
#      0  1  2  3   4      5 6 7
list1[0]=str(list1[0])
print("list1[0]=str(list1[0])")
print(list1)




