n,l = map(int,input().split())
water = list(map(int,input().split()))
water.sort()
cur = 0
cnt = 0
for i in water:
    if i > cur:
        cur = i+l-1
        cnt += 1
    
print(cnt)

