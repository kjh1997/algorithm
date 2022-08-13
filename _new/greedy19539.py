n = int(input())
s = list(map(int,input().split()))
T = sum(s)
if T % 3 != 0 :
    print('NO')
else:
    cnt = 0
    days = T // 3 
    for i in range(n):
        cnt+=s[i] // 2
    print("YES" if cnt >= days else "NO")