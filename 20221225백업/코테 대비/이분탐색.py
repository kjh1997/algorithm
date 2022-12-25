arr = [1,3,6,7,9,11,37,276,2134]

def bsearch(x):
    global arr
    s,e=0,len(arr)-1
    mid = -1
    while s<=e:
        mid = (s+e)//2
        if arr[mid] == x: return mid
        elif arr[mid] <=x: s = mid+1
        else: e=mid-1
    if arr[mid] == x:
        pass
    elif arr[mid] <= x:
        print(mid+1)
        arr = arr[:mid+1] + [x] + arr[mid+1:]
    elif arr[mid] >= x:
        print(mid)
        arr = arr[:mid] + [x] + arr[mid:]
        
print(bsearch(12))
print(arr)