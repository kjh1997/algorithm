import sys
input = sys.stdin.readline

data = input().strip()

for i in range(len(data)):
    if data[i:] == data[i:][::-1]:
        print(len(data)+i);exit()