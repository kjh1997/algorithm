
import sys
input = sys.stdin.readline
a = input().strip()
ans = set()
for i in range(1, len(a)+1):
    for j in range(0,len(a)-i+1):
        ans.add(a[j:j+i])

print(len(ans))