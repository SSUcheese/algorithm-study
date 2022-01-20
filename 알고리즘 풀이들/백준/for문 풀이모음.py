#2739번
'''
num = int(input())

for i in range(1, 10, 1):
    print(f'{num} * {i} = {num * i}')
'''   

#10950번

'''
repeat_num = int(input())

for i in range(repeat_num):
    num1, num2 = map(int, input().split())
    print(f'{num1 + num2}')
'''

#8393번

'''
num = int(input())

sum = 0

for i in range(num + 1):
    sum = sum + i

print(sum)
'''


#간단한 메모(자세한 내용은 onenote에 있음)
#앞으로 백준 풀면서 input()으로 받으면 시간초과가 일어날 수 있음. 그러니까 input = sys.stdin.readline 이거 쓰자

#15552번

'''
import sys

inp = int(input())
for i in range(inp):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)
'''

#2741번
#이런식으로 쓰면 역순으로 가능 다른 방식은 reversed(range(n)) 자세한 내용은 onenote에

'''
n = int(input())

for i in range(n, 0, -1):
    print(i)
'''

#11021번

'''
repeat_num = int(input())

for i in range(1, repeat_num + 1, 1):
    num1, num2 = map(int, input().split())
    print(f'Case #{i}: {num1 + num2}')
'''

#11022번

'''
repeat_num = int(input())

for i in range(1, repeat_num + 1, 1):
    num1, num2 = map(int, input().split())
    print(f'Case #{i}: {num1} + {num2} = {num1 + num2}')
'''

#2438번

'''
repeat_num = int(input())

for i in range(1, repeat_num + 1, 1):
    print('*' * i)
'''

#2439번
'''
repeat_num = int(input())

for i in range(1, repeat_num+1, 1):
    print(" " * (repeat_num-i) + "*" * i)
'''

#10871번
'''
size_num, max_num = map(int, input().split())

a = list(map(int, input().split()))
for i in range(size_num):
    if a[i] < max_num:
        print(a[i], end=" ")
'''

