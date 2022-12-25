import sys 
input = sys.stdin.readline

data = [0] * 41
data[1]=1
data[2]=1
def dp(num):
    if num==0: return 0
    if num==1: return 1
    if num==2: return 1
    if data[num] != 0: return data[num]
    data[num]=dp(num -1) + dp(num -2)
    return data[num]

t = int(input())
for test_case in range(1, t + 1):
    a = int(input())
    if a==0: print(1, 0)
    elif a==1: print(0, 1)
    else: print(dp(a-1), dp(a))