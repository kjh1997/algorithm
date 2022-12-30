import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

def div(a,b):
    print(a,b)
    if b == 1:
        return a%c
    
    tmp = div(a,b//2)
    if b % 2 ==0:
        return tmp*tmp %c
    
    else:
        return tmp*tmp*a %c
    
print(div(a,b))