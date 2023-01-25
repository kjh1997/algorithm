import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_m = [0 for _ in range(m)]
s = 0
num = 0
for i in range(n):
    s += arr_n[i]
    if s % m == 0:
        num += 1
    arr_m[s % m] += 1
for i in range(m):
    num += arr_m[i] * (arr_m[i] - 1) // 2
print(num)