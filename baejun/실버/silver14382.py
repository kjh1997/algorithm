n = int(input())
for i in range(n):
    x = int(input())
    data=[]
    cnt =0
    result = 0
    if x != 0:
        while len(data) != 10:
            cnt +=1
            data.extend(list(map(int,str(cnt * x))))
            data = list(set(data))
            if len(data)==10: result = x*cnt
        print(f"Case #{i+1}: {result}")
    else:
        print(f"Case #{i+1}: INSOMNIA")

