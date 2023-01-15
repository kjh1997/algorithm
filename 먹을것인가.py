import sys
input = sys.stdin.readline


for _ in range(int(input())):
    a, b = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))

    x.sort()
    y.sort()

    cur = 0
    ans = 0

    for i in range(a):
        
        while True:
            if cur == b or x[i] <= y[cur]:
                ans += cur
                break
            else:
                cur += 1
 
    print(ans)