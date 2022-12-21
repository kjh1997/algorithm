import sys

N = int(sys.stdin.readline())

for i in range(N):
    base = list(sys.stdin.readline().strip())
    if len(base) % 2 != 0: print("NO"); continue
    stack = []
    while len(base) != 0:
        stack.append(base.pop(0))
        if len(stack) < 2: continue
        if stack[-2:] == ["(",")"]: stack.pop();stack.pop()
    
    if len(stack) != 0: print("NO")
    else: print("YES")

