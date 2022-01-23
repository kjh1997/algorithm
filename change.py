T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    week = list(map(int,input().split()))
    cnt_day = 0
    
    lecture_cnt = 0
    open_week = week.count(1)
    week_cnt = 0
    if open_week >= num:
        sub_day = 0
        for i in week:
            cnt_day += 1
            lecture_cnt += i
            print(cnt_day, sub_day)
            if lecture_cnt == num:
                break
    else:
        week_cnt = num // open_week
        if num == week_cnt * open_week:
            cnt_day += (week_cnt-1) * 7 
            num -= (week_cnt-1) * open_week
            
        else:
            cnt_day += week_cnt * 7
            num -= week_cnt * open_week
        

        min_data = []
        for i in range(7):
            sub_day = 0
            week = week[:i] + week[i:]
            for i in week:
                sub_day += 1
                lecture_cnt += i
                if lecture_cnt == num:
                    min_data.append(sub_day)
                    break
        sub_day = min(min_data)
        
        

    print(f'#{test_case} {cnt_day+sub_day}')