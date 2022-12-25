T = int(input())
for test_case in range(1, T + 1):
    istr = input()
    if istr =="MON":
        result=6  
    elif istr =="TUE":
        result=5
    elif istr =="WED":
        result=4        
    elif istr =="THU":
        result=3    
    elif istr =="FRI":
        result=2    
    elif istr =="SAT":
        result=1    
    elif istr =="SUN":
        result=7    
    print(f"#{test_case} {result}")        
        
        
        
        
