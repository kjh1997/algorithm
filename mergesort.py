import sys
input = sys.stdin.readline

def merge(left,right):
    a,b=0,0
    ans=[]
    while True:
        if len(left) == 0 or len(right) == 0:break
        if left[0]<right[0]:
            ans.append(left.pop(0))
            a+=1
        elif left[0]>=right[0]:
            ans.append(right.pop(0))
            b+=1
    ans.extend(left)
    ans.extend(right)
    return ans


def sorting(arr):
    if len(arr) == 1: return arr
    
    mid = len(arr)//2
    left= arr[:mid]
    right = arr[mid:]
    left = sorting(left)
    right = sorting(right)
    return merge(left,right)
data = [int(input()) for i in range(int(input()))]
data.sort()
# data = sorting(data)
for i in data:
    print(i)