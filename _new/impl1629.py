import sys
a,b,c = map(int,sys.stdin.readline().split())
# (A^2) mod B = (A*A) mod B = ((A mod B) * (A mod B)) mod B
def multi (a,n):
    if n == 1:
        return a%c
    else:
        tmp = multi(a,n//2)
       
        if n %2 ==0:
            return (tmp * tmp) % c
        else:

            return (tmp  * tmp *a) %c
            
print(multi(a,b))