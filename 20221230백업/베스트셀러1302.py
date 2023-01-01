import sys
input = sys.stdin.readline
tc = int(input())
data = {}
for i in range(tc):
    x = input().strip()
    if x not in data: data[x]=1
    else: data[x]+=1
v = sorted(data,key=lambda x : data[x],reverse=True)
mv = max(data.values())
res = []
for i in v:
    if data[i]==mv: res.append(i)
    else: break
print(sorted(res)[0])