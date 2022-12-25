def check_data(cur):
    w =0
    cost =0
    for i in range(cur, len(arr)):
        if arr[i] != 0:
            w+=1
            cost = max(cost,arr[i])
            arr[i]=0
        else: break
    return cost * w
data=[]
maxN =0
for i in range(int(input())):
    s,e = map(int,input().split())
    maxN = max(maxN,e)
    data.append((s,e))
arr =[ 0 for i in range(maxN+1)]
for s,e in data:
    for i in range(s,e+1):
        arr[i] +=1
re =0
for i in range(len(arr)):
    if arr[i] != 0: 
        re += check_data(i)

print(re)


