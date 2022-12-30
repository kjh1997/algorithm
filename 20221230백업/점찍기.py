def solution(k, d):
    d=d**2
    answer = 0
    x,y = 0,0
    while True:

  
        dest = d - x**2        
        if dest < 0 : break    
        dest = int(dest**0.5)
        answer +=1+  (dest //k)
        
        x+=k

    return answer




print(solution(1,5))