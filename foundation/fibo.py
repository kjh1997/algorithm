cnt=0
def fibo(a):
    global cnt
    cnt+=14
    print(cnt)
    if a==1: return 1
    elif a==2: return 1
    else: return fibo(a-1)+fibo(a-2)

print(fibo(50))