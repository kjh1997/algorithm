# n = int(input())
# arr = [0 for i in range(n+1)]
# for i in range(1,n + 1):
#     day, value = map(int,input().split())
#     if i+day-1 > n: continue
#     arr[i+day-1] = max(max(arr[:i])+value,arr[i+day-1])
#     print(arr)
# print(max(arr))


n = int(input())
arr = [0 for i in range(n+1)]
for i in range(1, n +1):
    day, value= map(int,input().split())
    print(arr)
    if i + day -1 > n: continue
    arr[i+day-1] = max(max(arr[:i])+ value , arr[i+day-1])
    
print(max(arr))



