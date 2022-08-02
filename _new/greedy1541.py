arr = input().split('-')
re=0
for i in arr[0].split("+"):
    re+=int(i)
for i in arr[1:]:
    for j in i.split("+"):
        re -= int(j)
print(re)