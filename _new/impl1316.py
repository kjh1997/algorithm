tc = int(input())
arr = list(list(input()) for i in range(tc))


re = 0
for ar in arr:
    cnt = 0
    success = 0
    tmp=''
    for i in range(len(ar)):
        if tmp != ar[i]:
            if ar.count(tmp) != cnt: 
                success = 1
                break
            tmp = ar[i]
            cnt =1
        else:
            cnt +=1
    if success != 1: 
        re+=1

print(re)