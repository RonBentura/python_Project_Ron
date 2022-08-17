# range(1,6) - 1,2,3,4,5

for i in range(1,6):
    print("Hello")
    print(i)

print("=============================================")
# 2,3,4,5,6,7,8,9
for i in range(2,10):
    print(i)

print("=============================================")
# 0,1,2,3,4,5,6
for i in range(7):
    print(i)

print("=============================================")
# 3,5,7,9,11,13
for i in range(3,15,2):
    print(i)

print("=============================================")
for i in range(10,1,-1):
    print(i)

print("=============================================")
# Print all number from 100 to 1 that are divided by 3
for i in range(100,0,-1):
    if i%3==0:
        print(i)

print("=============================================")
# Print all number from 100 to 1 that are divided by 3
for i in range(99,0,-3):
    print(i)
