a = int(input())
def dis_sum(num):
    return num + sum(list(map(int,str(num))))

for i in range(a//2,a):
    if (a== dis_sum(i)): 
        print(i)
        break
    if (i==a-1): print(0)
