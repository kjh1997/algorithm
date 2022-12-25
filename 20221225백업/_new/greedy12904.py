before = list(map(str,input()))
after =list(map(str,input()))
while len(before) != len(after):
    if after[-1]=="A":
        after.pop()
    elif after[-1]=="B":
        after.pop()
        after= after[::-1]
print(1 if after==before else 0)