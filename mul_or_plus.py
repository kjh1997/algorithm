num = input()
cal = 0
for i in range(1,len(num)):
    print(num[i])
    if i == 1:
        if int(num[i-1]) * int(num[i]) > int(num[i-1]) +int(num[i]) :
            cal = int(num[i-1]) * int(num[i])
        else: 
            cal = int(num[i-1]) + int(num[i])
    else:
        if cal * int(num[i]) > cal + int(num[i]) :
            cal = cal* int(num[i])
        else:
            cal = cal+ int(num[i])
print(cal)