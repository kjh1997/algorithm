n=int(input())
distance=list(map(int, input().split())) # 거리
cash = list(map(int, input().split())) # 가격
re =0
cur = cash[0]
for i in range(n-1):
    if cur > cash[i]: 
        cur = cash[i]
    re = re + distance[i]*cur
print(re)

