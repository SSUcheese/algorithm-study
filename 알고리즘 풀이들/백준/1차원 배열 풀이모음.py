#10818번

'''
n = int(input())
num = map(int, input().split())
max = num[0]
min = num[0]

for i in num[1 : ]:
    if min > i:
        min = i
    elif max < i:
        max = i    
'''        
        
#2562번
'''a = list()
for i in range(9):
    b = int(input())
    a.append(b)

c = a[0]
    
for i in range(0, 9, 1):
    if c < a[i]:
        c = a[i]

print(c)
print(a.index(c) + 1)'''

#2577번
'''
a = int(input())
b = int(input())
c = int(input())

total = a * b * c

total = str(total)

for i in range(0, 10, 1):
    print(total.count(f'{i}')) #format함수 안 쓰고 str()이거 활용도 ㄱㅊ음
'''

#3052번

'''a = []

for i in range(10):
    n = int(input())
    n = n % 42
    a.append(n)
a = set(a)
print(len(a))'''


#1546번
'''num = int(input())
a = list(map(int, input().split()))
b = []
mean = 0

for i in range(0, num, 1):
    b.append(a[i] / max(a) * 100) 

mean = sum(b) / len(b)
print(mean)'''

#8958번

'''num = int(input())


for i in range(num):
    score = 0
    total = 0
    a = input()
    
    for h in range(0, len(a), 1):
        if a[h] == 'O':
            score += 1
            total = total + score
        elif a[h] == 'X':
            score = 0
    print(total)'''
