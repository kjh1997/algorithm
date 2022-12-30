import sys
input = sys.stdin.readline

ans = []
while True:
    data = list(input())
    stack = []
    if "-" in data: break
    count =0
    for i in data:
        if i == "}" and not stack: count +=1; stack.append("{")
        elif i == "}" and stack: stack.pop()
        elif i == "{": stack.append(i)
    count += len(stack)//2
    ans.append(count)
        

for num,i in enumerate(ans):
    print('{}. {}'.format(num+1,i))