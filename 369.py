num = int(input())
change_data = ""
for i in range(1,num+1):
    cnt = 0
    x = ""
    cnt += str(i).count('3')
    cnt += str(i).count('6')
    cnt += str(i).count('9')
    if cnt > 0:
        for i in range(cnt):
            x += '-'
    else:
        x = str(i)
    change_data += x + " "

print(change_data)
