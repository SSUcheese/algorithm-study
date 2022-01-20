#10952번
'''
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break
 '''   
    
#1110번

num = int(input())
n = num
count = 0

while True:
    a = num // 10
    b = num % 10
    c = (a+b) % 10
    num = (b * 10) + c
    
    count += 1
    if (num == n):
        break
print(count)
    