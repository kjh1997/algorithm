a, b = map(int, input().split())
coin = [int(input()) for i in range(a)]
cnt = 0
for i in coin[::-1]:
    cnt += b//i
    b = b % i
print(cnt)