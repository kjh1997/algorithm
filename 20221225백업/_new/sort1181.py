import sys
tc = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(tc)]
data = list(set(data))
data.sort()
data.sort(key = len)
for i in data:
    print(i)
