list1 = []
for i in range(3):
    num = int(input('enter number: '))
    list1.append(num)
print(list1)

print(f'the highest number is: {max(list1)}')
print(f'the lowest number is: {min(list1)}')
print(f'the average of the numbers is: {sum(list1)/ len(list1)}')

