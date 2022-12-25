# s = input()
# c4 = input()
# while c4 in s:
#     s= s.replace(c4,"")
# print("FRULA" if s == "" else s)
s = input()
c4 = input()
stack=[]
l = len(c4)
for i in s:
    stack.append(i)
    if i == c4[-1] and ''.join(stack[-l:]) == c4:
        del stack[-l:]

print("FRULA" if ''.join(stack) == "" else ''.join(stack))