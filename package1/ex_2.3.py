C=(input('how many pc did you treat today? '))

if C=='':
    C=15
    print(f'tomorrow you will have to treat {C * 2} pcs')
else:
    print(f'tomorrow you will have to treat {int(C) * 2} pcs')
