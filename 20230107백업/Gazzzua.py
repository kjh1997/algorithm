import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))
data.reverse()
ans=0
top = data[0]
for i in data[1:]:
    if top < i: top = i
    else: ans += top - i
print(ans)

