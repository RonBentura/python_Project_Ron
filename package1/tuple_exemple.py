t1=(10,11,12,13,"abc")

print("t1[2]",t1[2])

t1+=(100,200,300)
print(t1)

t1+=(400,)
print("t1+=(400,)",t1)

a,b,c = 10,20,30
print("a,b,c = 10,20,30")
print(a,b,c)

a,b=b,a
print("a,b=b,a")
print(a,b)

list1=list(t1)
print("list1=list(t1)")
print(list1)
list1[3]=15
print(list1)
t1=tuple(list1)
print("t1=tuple(list1)")
print(t1)