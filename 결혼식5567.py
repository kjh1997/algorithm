import sys
input = sys.stdin.readline

N = int(input())
tc = int(input())
visit = []
data = {}
for i in range(tc):
    n,m=map(int,input().split())
    if n not in data: data[n]=set()
    if m not in data: data[m]=set()
    data[n].add(m)
    data[m].add(n)

def search(q, depth):
    if depth > 2: return
    visit.append(q)
    for i in data[q]:
        search(i, depth +1)
        
if 1 not in data: print(0); exit()
search(1,0)
ans = set(visit)
ans.remove(1)
print(len(ans))
