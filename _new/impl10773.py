arr=[]
for i in range(int(input())):
    num = int(input())
    if num==0:
        arr.pop()
    else:
        arr.append(num)
print(sum(arr))