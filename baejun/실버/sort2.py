import sys
num = int(input())
a = sorted([int(sys.stdin.readline()) for i in range(num)], reverse=True)
for i in a[::-1]:print(i)
