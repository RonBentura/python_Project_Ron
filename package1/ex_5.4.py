word=input('enter sentence: ')
#a
print(len(word))
print('====================================')
#b
print(word[2:6])
print('====================================')
#c
word=word.split()
print(word[0], word[0], word[0])
print('====================================')
#d
lord=input('enter a word: ')
lord=lord.split()
for i in range(len(lord)):
    lord[i]=lord[i].capitalize()
print(*lord)
print('====================================')
#d
ford=input('enter sentence: ')
print(ford.title())






