import sys 
input = sys.stdin.readline

t = int(input())
for test_case in range(1, t + 1):
    a,b = map(int,input().split())
    print(str(a**b)[-1])