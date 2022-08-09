n = int(input())
arr = list(map(int,input().split()))
x = arr.pop(arr.index(max(arr)))
re = (len(arr)*x)+sum(arr)
print(re)

