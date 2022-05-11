N = int(input())
data = []

for _ in range(N):
  start, end = map(int, input().split())
  data.append((start, end))

data = sorted(data, key=lambda a: a[0]) 
data = sorted(data, key=lambda a: a[1]) 
end=0
start=0
cnt =0
for x,y in data:
    if end <=x:
        cnt+=1
        end,start=y,x
print(cnt)
