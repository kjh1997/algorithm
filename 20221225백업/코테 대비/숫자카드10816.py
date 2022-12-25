import sys

N = int(sys.stdin.readline())
data = sorted(list(map(int,sys.stdin.readline().split())))
M = int(sys.stdin.readline())
findUs = list(map(int,sys.stdin.readline().split()))

dictData = {}
for i in data:
    if i not in dictData: dictData[i] = 1
    else: dictData[i] +=1

for i in findUs:
    if i in dictData: print(dictData[i], end=" ")
    else: print(0, end=" ")
