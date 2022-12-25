num,result = int(input()),0
data = sorted(list(map(int,input().split())))
for i in range(len(data), -1, -1):
    result += sum(data[:i])
print(result)
