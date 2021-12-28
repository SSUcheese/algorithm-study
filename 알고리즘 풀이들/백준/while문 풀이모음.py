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
n = 0
x = input()
y = x
while True:
    first = str(int(x[0]) + int(x[1]))
    first = first[0]
    tenth = x[1]
    x = tenth + first
    n += 1
    if int(x) == int(y):
        break
print(x)

print("3" + "4")
    