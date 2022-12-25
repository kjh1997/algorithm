N = int(input())
p = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            p[i][j] = 1
result = 0
for i in p:
    result += i.count(1)
print(result)