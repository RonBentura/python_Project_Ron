age = int(input('enter age: '))

while 0<=age<=120:
    if 0 <= age <= 18:
        print('child')
    elif 19 <= age <= 60:
        print('adult')
    elif 61 <= age <= 120:
        print('senior')
    age = int(input('enter age: '))