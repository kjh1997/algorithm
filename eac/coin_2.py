num = input()
list_coin = list(map(int,input().split()))
cnt = 1
print("1")
while True:
    chk = 0
    for i in range(len(list_coin)):
        list_coin = list_coin[i:] + list_coin[:i]
        data = 0
        
        for i in list_coin:
            data += i
            if data == cnt:
                chk =1
                break
    if chk == 1:
        cnt +=1
    if chk != 1:
        break
print(cnt)

