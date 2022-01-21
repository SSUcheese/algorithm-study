#1712번

'''a, b, c = map(int, input().split())
i = 0

if c > b:
    while (c * i) < (a + (b * i)):
        i += 1
    print(i+1)
else:
    print(-1)''' #이런식으로 풀면 시간초과로 탈락임
    
#간단한 방정식을 구성해서 푸는 방식이 효율적이고 빠르다  

'''a, b, c = map(int, input().split())

if c> b:
    print(int(a/(c-b)+1))
else:
    print(-1) ''' 
    
#2869번
'''import math
a, b, v = map(int, input().split())

n = math.ceil((v - b) / (a - b))
print(n)'''