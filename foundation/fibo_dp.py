a = [0]*100
def dp_fibo(x):
    if x==1:return 1
    elif x==2: return 1
    elif a[x] != 0: return a[x]
    else: 
        a[x] = dp_fibo(x-1) + dp_fibo(x-2)
        return a[x]

print(type(dp_fibo(99)))
print(a)