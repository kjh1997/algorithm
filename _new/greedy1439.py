
s = input()

prv = "x"
cnt = 0
for i in s:
    if prv != i:
        cnt +=1
        prv = i
print(cnt//2)