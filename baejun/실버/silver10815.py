from re import M
import sys

def search(arr, t):
    s=0
    e=a-1
    while s<=e:
        m = (s + e) //2
        if arr[m] == t: return 1
        elif arr[m]> t: e = m -1
        else: s = m + 1
    return 0

a = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))
b = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in arr:
    print(search(sorted(card), i), end=" ")