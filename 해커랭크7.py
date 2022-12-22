def appendAndDelete(s, t, k):
    # Write your code here
    cnt = 0
    for i,j in zip(s,t):
        if i ==j: cnt +=1; continue
        else: break
    l1 = len(s)
    l2 = len(t)
    if l1+l2 - (2*cnt) <= k and (l1+l2)%2==k%2:  return "YES"
    else: return "NO"

print(appendAndDelete(["y"],["y","u"],2))