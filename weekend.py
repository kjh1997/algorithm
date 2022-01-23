T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    week = list(map(int,input().split()))
    cnt_day = 0
    lecture_cnt = 0
    open_week = week.count(1)
    week_cnt = 0
    if open_week >= num:
        for i in week:
            cnt_day += 1
            lecture_cnt += i
            if lecture_cnt == num:
                break
    else:
        week_cnt = num // open_week
        week_cnt = num // open_week
        if num == week_cnt * open_week:
            cnt_day += (week_cnt-1) * 7 
            num -= (week_cnt-1) * open_week
            
        else:
            cnt_day += week_cnt * 7
            num -= week_cnt * open_week
        

        
        for i in week:
            cnt_day += 1
            lecture_cnt += i
            if lecture_cnt == num:
                break

    print(f'#{test_case} {cnt_day}')
