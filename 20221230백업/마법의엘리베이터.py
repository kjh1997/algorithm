def solution(storey):
    ans = 0 
    while storey:
        div = storey % 10
        if div == 5 and storey//10%10 >= 5 or div >5:
            storey += 10
            ans += 10-div
        else: ans +=div
        storey=storey//10
    return ans

    

print(solution(6666))