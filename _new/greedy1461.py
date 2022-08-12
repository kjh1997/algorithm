n,m=map(int,input().split())
book=list(map(int,input().split()))
plus=[]
minus =[]
max_book=0

for i in book:
    if i <0: minus.append(i)
    elif i >0: plus.append(i)
    if abs(i) > abs(max_book):
        max_book=i

plus.sort(reverse=True)
minus.sort()
re = 0
for i in range(0,len(plus),m):
    if max_book == plus[i]: continue
    re += plus[i]
for i in range(0,len(minus),m):
    
    if max_book == minus[i]: continue
    re += abs(minus[i])


print((re*2)+abs(max_book))
