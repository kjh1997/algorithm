a1 = list(map(str,input()))
a2 = list(map(str,input()))
l1, l2 = len(a1),len(a2)
cache = [0 for i in range(l2)]

for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]:
            cnt=cache[j]
        elif a1[i]==a2[j]:
            cache[j]= cnt+1
print(max(cache))


