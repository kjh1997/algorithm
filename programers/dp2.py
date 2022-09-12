def solution(n):
    dp = [0]*(2001)
    dp[0],dp[1],dp[2]=0,1,2
    cnt = 3
    if n<3:
        return dp[n]
    while cnt!=n+1:
        
        dp[cnt]=dp[cnt-1]+dp[cnt-2]
        cnt+=1
    
    
    return dp[n] %1234567

print(solution(1))