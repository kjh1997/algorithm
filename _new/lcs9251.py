a = list(map(str,input()))
b = list(map(str,input()))
arr = [0] * len(b)
for i in range(len(a)):
    tmp = 0
    for j in range( len(b)):
        if tmp < arr[j]:
            tmp = arr[j]
        elif a[i] == b[j]:
            arr[j]= tmp +1
print(max(arr))