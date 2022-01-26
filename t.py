import sys
import time
N = 5
cnt = 0
x = 0
def iter(N, M, arr):
    kri = []
    if len(arr) == 2:
        tmp = []
        for i in arr: tmp.append(i)
        return tmp
    
    if M != -1: arr.append(M)

    for i in range(1, N+1):
        arr.append(i)
        kri.append(iter(N, M, arr))
        arr.remove(i)
    print(kri)
    return kri

def check(N, arr1, arr2):
    #under
    if arr1[1] == arr2[1]: return True
    #diagonal
    elif abs(arr1[0] - arr2[0]) == abs(arr1[1] - arr2[1]): return True
    else: return False

def solve(N, k, arr, cands):#k는 증가된 상태로 와야, 즉 현재 볼 것.
    if len(arr) == N:
        global cnt
        cnt += 1
        return
    global x
    x +=1
    print(x,"cands", cands)
    for i in cands[k+1:]:
        if len(i) == 0: return

    for i in range(k+1, N):
        tmp = []
        
        for j in range(len(cands[i])):
            if check(N, arr[-1], cands[i][j]) == False: tmp.append(cands[i][j])
        cands[i] = tmp

    for i in cands[k+1]:
        arr.append(i)
        solve(N, k+1, arr, list(cands))
        arr.remove(i)


cands = iter(N, -1, [])

for i in cands[0]:
    tmp = list(cands)
    tmp[0] = i
    solve(N, 0, [i], tmp)

print(cnt)

# #another version(정석)
# """
# N = int(input())
# #백트래킹
# def solve(i, q):
#     p = [True for i in range(N+1)]
    
#     #이거 한줄 빼먹어서 틀리고 있었음.
#     p[0] = False
#     for x in range(1, i):
#         p[q[x]] = False
#         if q[x] + i - x <= N:
#             p[q[x] + i - x] = False
#         if q[x] - i + x >= 1:
#             p[q[x] - i + x] = False
    
#     rst = 0
#     for j in range(len(p)):
#         if p[j] == True:
#             if i == N:
#                 global cnt
#                 rst += 1
#             else:
#                 q[i] = j
#                 rst += solve(i+1, q)
#     return rst
# res = solve(1, [True for _ in range(N+1)])
# print(res)