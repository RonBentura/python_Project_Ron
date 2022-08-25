from random import randint

g=[]
for i in range(10):
    g.append(randint(1,100))

print(g)

g_pass=0
g_failed=0
for gr in g:
    if gr>=60:
        g_pass+=1
    else:
        g_failed+=1

print(f'{g_pass} tests passed')
print(f'{g_failed} test failed')
