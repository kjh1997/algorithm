import sys

input = sys.stdin.readline




n = int(input())
arr = list(map(int,input().split()))
map = [0 for i in range(n)]
cnt =0
for i in range(1, n+1):
    cnt =0
    j = 0
    while True:
        if map[j]==0:
            
            if cnt == arr[i-1]:
                map[j] = i
                break
            cnt +=1
        j +=1
print(*map)