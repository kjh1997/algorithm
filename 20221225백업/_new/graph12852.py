from collections import deque

def sol(n):
    q = deque()
    q.append((n,[n]))

    visit =set()
    visit.add(n)


    while q:
        cur, moving = q.popleft()
        if cur == 1: 
            print(len(moving)-1)
            print(" ".join(map(str,moving)))
            return
        if cur % 3 == 0 and cur % 3 not in visit:
            nmoving = moving.copy()
            d = cur//3
            visit.add(d)
            nmoving.append(d)
            q.append((d, nmoving))
        if cur % 2 == 0 and cur % 2 not in visit:
            nmoving = moving.copy()
            d = cur//2
            nmoving.append(d)
            visit.add(d)        
            q.append((d, nmoving))
        if cur -1 not in visit:
            nmoving = moving.copy()
            d = cur -1
            nmoving.append(d)
            visit.add(d)
            q.append((d, nmoving))

sol(int(input()))