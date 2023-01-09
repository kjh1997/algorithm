import sys
from collections import deque
input = sys.stdin.readline


n,m = map(int,input().split())


q = deque()
p,w=map(int,input().split())
for i in range(n-1):
    q.append(list(map(int,input().split())))
tmp =[]

container = []
maxNum = 0
ans =0
while True:
    p,w = q.popleft()
    
    



