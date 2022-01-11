#11654번

'''num = input()
print(ord(num))'''


#11720번

'''a= input()
num = input()
add = 0
c = 0

for i in range(0, len(num), 1):
    c = int(num[i])
    add += c
print(add)'''   

#10809번

'''abc= 'abcdefghijklmnopqrstuvwxyz'

word = input()

for i in abc:
    if i in word:
        print(word.index(i), end=' ')
    else:
        print(-1, end=' ')'''
        
#2675번

'''repeat_num = int(input())

for i in range(repeat_num):
    r1, word1 = input().split()
    r1=int(r1)
    for i in word1:
        print(f'{i*r1}', end='')
    print(end='\n')'''