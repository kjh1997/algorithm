num = int(input())
a = sorted(list(map(int, input().split())))
if num == 1: print(a[0]**2)
else: print(a[0]*a[-1])
