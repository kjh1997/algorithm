t = int(input()) # 테스트 케이스
for i in range(t):
    avg_data = []
    input_num, peo = map(int,input().split())
    qual = input_num/10
    for j in range(input_num):
        data = list(map(int, input().split())) # 테스트 10명단위
        avg_data.append(data[0]*0.35+data[1]*0.45+data[2]*0.2)
    grade = avg_data[peo-1]
    sort_list = sorted(avg_data, reverse=True) 
    grade_data = sort_list.index(grade)
     
    if int(grade_data/qual) == 0: result_value = 'A+'
    elif int(grade_data/qual) == 1: result_value = 'A0'
    elif int(grade_data/qual) == 2: result_value= 'A-'
    elif int(grade_data/qual) == 3: result_value= 'B+'
    elif int(grade_data/qual) == 4: result_value= 'B0'
    elif int(grade_data/qual) == 5: result_value= 'B-'
    elif int(grade_data/qual) == 6: result_value= 'C+'
    elif int(grade_data/qual) == 7: result_value= 'C0'
    elif int(grade_data/qual) == 8: result_value= 'C-'
    elif int(grade_data/qual) == 9: result_value= 'D0'          
    print(f"#{i+1} {result_value}")