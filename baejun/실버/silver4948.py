import sys 
import math
input = sys.stdin.readline
data = [0] * 123456*2
while(True):
    t = int(input())
    if(t==0): break
    cnt =0
    for i in range(t+1,2*t+1):
        for j in range(1, int(math.sqrt(i))+1):
            if i%j == 0:
                cnt +=1
                break





    