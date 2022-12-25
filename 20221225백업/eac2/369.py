s = ["3","6","9"]
for i in range(1, int(input())+1):
    if s[0] in str(i) or s[1] in str(i) or s[2] in str(i):     
        for j in s: 
            for k in range(str(i).count(j)): print("-",end="")
        print(" ",end="")
    else: print(i,end=" ")