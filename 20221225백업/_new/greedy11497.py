re = []
for i in range(int(input())):
    n = int(input())
    tmp = 0
    base = [0 for i in range(n)]
    arr = list(map(int, input().split()))
    arr.sort()
    base[0]=arr[0]
    for i in range(1,n):
        if i % 2 !=0:
            base[-((i//2)+(i%2))]=arr[i]
        else: base[((i//2)+(i%2))]=arr[i]
    for i in range(-1,n):
        tmp=max(tmp, abs(base[i-1]-base[i]))
    re.append(tmp)
for i in re:print(i)