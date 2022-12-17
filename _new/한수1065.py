import sys

N = int(sys.stdin.readline())

if N <=99:
    print(N)
else:
    result = 99
    for i in range(101, N+1):
        num = list(map(int,str(i)))
        if num[0]-num[1] == num[1] - num[2]:
            result +=1
    print(result)


