a = [1,5,2,7,9,0,3,32,26,10,21]
import sys
sys.setrecursionlimit(10**7)

def bubblesort(arr,length):
    for i in range(length):
        for j in range(1,length):
            if arr[j-1] > arr[j]: 
                arr[j-1],arr[j]=arr[j],arr[j-1]  
    return arr

def merge(left,right):
    arr = []
    i,j=0,0
    while i<len(left) and j <len(right):
        
        if left[i] < right[j]:
            arr.append(left[i])
            i+=1
        else:
            arr.append(right[j])
            j+=1
    arr+=left[i:]
    arr+=right[j:]
    return arr

def mergesort(arr):
    print(arr)
    if len(arr)<=1: return arr
    mid = len(arr)//2
    
    left = arr[:mid]
    right = arr[mid:]
    leftArr = mergesort(left)
    rightArr= mergesort(right)
    return merge(leftArr,rightArr)

print(mergesort(a),"?")