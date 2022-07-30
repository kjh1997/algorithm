from itertools import combinations
while(True):
    
    b = list(map(str, input().split()))
    if b[0] =="0": break
    b.pop(0)
    for i in list(map(list,combinations(b,6))):
        print(" ".join(i))
    print(" ")
    

