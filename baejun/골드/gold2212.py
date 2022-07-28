a = int(input())
b = int(input())
c = list(map(int,input().split()))
c.sort()
if a<= b: print(0)
else:
    d = []
    for i in range(1,len(c)):
        d.append(abs(c[i]-c[i-1]))
    d.sort()
    for i in range(b-1):
        d.pop()
    print(sum(d))