n = int(input())
t= []
p=[]
for i in range(n):
    _,__ = map(int, input().split())
    t.append(_), p.append(__)
dp=[0 for i in range(n+1)]
temp=0
for i in range(n):
    temp=max(temp,dp[i])
    if i+t[i] > n: continue
    dp[i+t[i]] = max(temp+p[i],dp[i+t[i]])
print(max(dp))
