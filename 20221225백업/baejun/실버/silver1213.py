# # import string
data ={}
s = input()
lenS = len(s)
evenAlpha = ""
re=""
for i in range(lenS):re+="0"
even = 0
for i in s:
    cnt = s.count(i)
    if cnt==0: continue
    if cnt % 2 !=0: even+=1; evenAlpha=i
    data[i]=cnt
    s=s.replace(i,"")
keyData = sorted(data.keys())
if even >1: print("I'm Sorry Hansoo")
else:
    re = ""
    center = evenAlpha
    for k,v in sorted(data.items()):
        for i in range(v//2):
            re += k
    print(re+ center + re[::-1])

