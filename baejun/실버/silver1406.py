# import sys
# data = input()
# l = list(map(str,data)) 
# a = int(input())
# cur = len(l)
# for _ in range(a):
#     s = input()
#     if s[0] =="P":
#         l.insert(cur, s[-1])
#         cur +=1 
#     elif s[0] =="L": 
#         if cur >0: 
#             cur -= 1
#     elif s[0] =="D": 
#         if cur <len(l):
#             cur +=1
#     else:
#         if cur >0: 
#             l.remove(l[cur-1])
# print("".join(l))


# import sys
# input = sys.stdin.readline
# data = input().strip()
# l = list(map(str,data)) 
# a = int(input().strip())
# cur = len(l)
# for _ in range(a):
#     s = input().strip()
#     if(cur ==0 and s[0]=="B")or \
#     (cur ==0 and s[0]=="L") or \
#         (cur == len(l) and s[0]=="D"): continue
#     if s[0] =="P":
#         l.insert(cur, s[-1])
#         cur +=1
#     if s[0] =="L": 
#         if cur >0: 
#             cur -= 1
#     if s[0] =="D": 
#         if cur <len(l):
#             cur +=1
#     if s[0] =="B":
#         if cur >0: 
#             cur -= 1
#             l.pop(cur)
# print("".join(l), end="")

import sys

st1 = list(sys.stdin.readline().rstrip())
st2 = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
    
    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())

    elif command[0] == 'B':
        if st1:
            st1.pop()
            
    else:
        st1.append(command[1])  

st1.extend(reversed(st2))
print(''.join(st1))

