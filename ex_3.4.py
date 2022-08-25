from random import randint

input('whink of number between 0-100... press eneter when ready')

count = 1
low = 0
high = 100

num = randint(0,100)
answer = input(f'my guess is: {num}, if too high, press h, too low - l , correct - c')

while answer != 'c':
    if answer == 'l:':
        low=num+1
        num = randint(low,high)
    elif answer == 'h':
        high=num-1
        num + randint(low,high)
    else:
        print('invalid answer!!!')
        answer = input(f'my guess is: {num}, if too high, press h, too low - l , correct - c')
        continue

    count+=1
    answer = input(f'my guess is: {num}. if too high, press h, too low - l , correct - c')

print(f'gg number of trials: {count}')
