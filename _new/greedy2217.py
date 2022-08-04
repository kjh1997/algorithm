n = int(input())
arr = [int(input()) for i in range(n)]
re=[]
arr.sort()
l=len(arr)
for i in range(len(arr)):
    re.append(arr[0]*len(arr))
    arr.pop(0)
print(max(re))