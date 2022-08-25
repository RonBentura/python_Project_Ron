d1 = {"Dan": 30, "Gal": 70, 3: 100, "Gali": 75, 1: 68, "Moshe": 70}
a = input('enter key: ')
if a.isnumeric():
    a = int(a)
if a in d1:
    print('exists')
else:
    print('doesnt exists')
