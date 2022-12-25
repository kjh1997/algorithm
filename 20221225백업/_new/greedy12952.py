from collections import deque
n = int(input())
q = deque()
q.append((n,[n],0))

visit=[n]
while True:
    data,arr,cnt = q.popleft()
    if data ==1:
        print(cnt)
        for i in arr:
            print(i,end=" ")
        exit()
    if data % 3 == 0 and data % 3 not in visit:
        arr.append(data // 3)
        ar2 = arr.copy()
        q.append((data // 3, ar2,cnt+1))
        visit.append(data // 3)
        arr.pop()
    if data % 2 == 0 and data % 2 not in visit:
        arr.append(data // 2)
        ar3 = arr.copy()
        q.append((data // 2, ar3,cnt+1))
        visit.append(data // 2)
        arr.pop()
    if data-1 not in visit:    
        arr.append(data -1)
        ar4 = arr.copy()
        q.append((data -1, ar4,cnt+1))
        visit.append(data -1)
        arr.pop() 11