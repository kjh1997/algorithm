def combinations(arr, al):
    if len(se) == al and sum(se) ==K:
        re.append(list(se))
        return

    start = len(vi)-vi[::-1].index(1)-1 if vi.count(1) != 0 else 0
    for i in range(start, len(arr)):
        if vi[i] ==0:
            se.append(arr[i])
            vi[i] =1
            combinations(arr,al)
            se.pop()
            vi[i]=0

for tc in range(int(input())):
    se,re = [],[]
    N, K=map(int, input().split())
    arr = list(map(int, input().split()))
    vi = [0 for _ in range(len(arr))]  
    ST1 = arr.count(K)  
    for i in range(2,len(arr)+1): combinations(arr,i)
    print(f'#{tc+1} {len(re)+ST1}')
### 위에는 내가 푼 것    
def solve(idx, sum):
    global cnt
    if idx >= N:         
        return
    temp = sum + A[idx]
    if temp == K:
        cnt += 1
    
    solve(idx + 1, sum)
    solve(idx + 1, temp)
 
T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = 0
    solve(0, 0)
    print("#{} {}".format(i+1, cnt))