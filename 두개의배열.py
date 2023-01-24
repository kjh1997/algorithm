import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    A, B = list(map(int, input().split())),list(map(int, input().split())) 
    B.sort()
    cnt = 0

    for a in A:
        s, e = 0, M-1
        while s < e:
            m = (s+e)//2
            if B[m] <= a:
                s = m + 1
            else:
                e = m
        if s == 0:
            cnt += B[0]
        else:
            cnt += B[s] if a - B[s-1] > B[s] - a else B[s-1]
    print(cnt)