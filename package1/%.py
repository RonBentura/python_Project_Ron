#num1=int(input("enter number 1: "))
#num2=int(input("enter number 2: "))

#print(num1%num2)

num3=int(input("enter number with 3 digits: "))
# 459

print("right digit", num3%10)

#print("let digit", int(num3/100))
print("left digit", num3//100)


#print("middle digit", num3%100//10)
print("middle digit", num3//10%10)