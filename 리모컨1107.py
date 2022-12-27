import sys
input = sys.stdin.readline

N = int(input())
BN = int(input())
broken = list(map(str,input().split()))

ans = abs(100-N)

for i in range(1000001):
    num = str(i)
    chk = 0
    for j in num:
        if j in broken:
            chk=1
            break

    if chk != 1:
        ans = min(ans, abs(int(num)-N)+len(num))

print(ans)