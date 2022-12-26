import sys
paren_lst = list(sys.stdin.readline().strip())
stack = []
pre = ''
pair = {')': '('}
ptr = 0
ans = 0
for par in paren_lst:
    if par in '(':
        stack.append(par)
        ptr+=1
    elif stack:
        if par == ')':
            ptr-=1
        if stack[-1] == pair[par]: 
            stack.pop()
            if pre == pair[par]: 
                ans += ptr
            else:
                ans += 1
    pre = par
print(ans)