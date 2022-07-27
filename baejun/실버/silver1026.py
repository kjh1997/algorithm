import sys 
input = sys.stdin.readline

t = int(input())
a = list(map(int, input().split())) 
b = list(map(int, input().split()))
c = b.copy()
d=[]
a.sort()
sum=0
for i in range(len(b)):
    max_value = b.pop(b.index(max(b)))
    sum += a[i] * max_value

print(sum)

