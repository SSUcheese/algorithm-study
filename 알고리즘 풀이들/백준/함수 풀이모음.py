#15596번

'''def solve(a):
    return sum(a)'''

#4673번
'''delete_num = []
numbers = list(range(1, 10001,1))

for num in numbers:
    for n in str(num):
        num = num + int(n)
    if num <= 10000:
        delete_num.append(num)
        
for delete in set(delete_num):
    numbers.remove(delete)
for i in numbers:
    print(i) '''  
