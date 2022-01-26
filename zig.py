num = int(input())
result = 0
for i in range(1,num+1):
    if i //2 == i/2:  result += i
    else: result -= i
print(result)
