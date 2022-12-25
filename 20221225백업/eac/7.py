T = int(input())
for test_case in range(1, T + 1):
    cal, chk = input(),0
    year,month, day = cal[:4],cal[4:6],cal[6:]
    if month == "01" or month == "03" or month == "05" or month == "07" or month == "08" or month == "10" or month == "12":
        if int(day) > int(31) or int(day) <1: chk = 1
    elif month == "02": 
        print("!@#!@#")
        print(day)
        if int(day) > 28 and int(day) < 1: chk =1
    else: 
        if int(day) > 30 and int(day) < 1: chk =1

    if chk == 0 :result = year+'/'+ month+'/'+day
    else: result=-1
    print(f"#{test_case} {result}")
