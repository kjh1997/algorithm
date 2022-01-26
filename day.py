a = list(map(int, input().split()))
day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 , 31]
result = 0

if a[0] == a[2]:
    result = a[3] - a[1] +1 
else:
    result = sum( day[ a[0] : a[2]-1 ] ) + day[a[0]-1] - a[1] + day[a[2] -1] - a[3] + 2
print(result)



