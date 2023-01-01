import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = list(input())
ans = 0
for i in range(n):
    if data[i] == 'P':
        for i in range(max(i-k, 0), min(i+k+1, n)):
            if data[i] == 'H':
                data[i] = 0
                ans += 1
                break
print(ans)