import sys
input = sys.stdin.readline
sr = input().strip()
N  = int(input())
arr = [0] * len(sr)
tc = [ list(map(str,input().split())) for i in range(N)]
S = tc[0][0]
cnt = 0
for i in range(len(sr)):
    if sr[i] == S: cnt +=1
    arr[i]=cnt
for t in tc:
    if t[1]=="0": print(arr[int(t[2])]); continue
    print( arr[int(t[2])] - arr[int(t[1])-1] ) 


