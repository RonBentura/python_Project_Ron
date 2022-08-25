d1={}
a = input('enter key: ')
if a.isnumeric():
    a = int(a)

for a in d1:
    d1[a]=[a*a]
    d1.update()
print(d1)

