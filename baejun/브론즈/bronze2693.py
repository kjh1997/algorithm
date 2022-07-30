def sort_bubble(arr):
    cnt=0
    for i in range(10):
        for j in range(1,10):
            cnt+=1
            if arr[j-1]>arr[j]: 
                arr[j-1],arr[j]=arr[j],arr[j-1]
            print(arr, cnt)

    print(arr)



for i in range(int(input())):
    arr = list(map(int,input().split()))
    sort_bubble(arr)

def bsearch(arr, t, s, e):
    if s > e: return None
    mid = (s+e)//2
    if arr[mid]==t: return mid
    elif arr[mid]>t: s=mid+1
    else: e=mid-1