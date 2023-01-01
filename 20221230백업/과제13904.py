import sys
input = sys.stdin.readline
tc = int(input())
data = [list(map(int,input().split())) for i in range(tc)]
data = sorted(data, key= lambda x: x[1], reverse=True)
ans = 0
visit = [False for i in range(1002)]
for i in data:
    for j in range(i[0]-1,-1,-1):
        if visit[j] == False:
            visit[j]=i[1]
            ans += i[1]
            break
print(ans)