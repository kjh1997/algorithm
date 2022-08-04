import sys
input = sys.stdin.readline
n = int(input())
arr=[]
for i in range(n):
    a = list(map(str,input().split()))
    if a[0] == "push_back":
        arr.append(a[1])
    if a[0] == "push_front":
        arr.insert(0, a[1])
    if a[0] == "front":
        print(arr[0] if len(arr) != 0 else -1)

    if a[0] == "back":
        print(arr[-1] if len(arr) != 0 else -1)

    if a[0] == "size":
        print(len(arr))
    
    if a[0] == "empty":
        print(1 if len(arr) == 0 else 0)
        
    if a[0] == "pop_back":
        print(arr.pop() if len(arr) != 0 else -1)

    if a[0] == "pop_front":
        print(arr.pop(0) if len(arr) != 0 else -1)