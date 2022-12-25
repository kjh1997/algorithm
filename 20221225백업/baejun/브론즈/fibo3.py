import sys
sys.setrecursionlimit(10**7)
def dp(num):
    global data, cnt0, cnt1
    if num==0: return 0;cnt0+=1
    if num ==1: return 1;cnt1+=1
    if num ==2: return 1
    if data[num] != 0: return data[num]
    data[num] = dp(num-1)+dp(num-2)
    return data[num]
cnt0=0
cnt1=0
data = [0]*21
dp(int(input().rstrip()))
print(cnt0, cnt1)

