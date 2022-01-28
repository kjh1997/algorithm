from operator import index


num = input()
x = 0
for i in range(1, len(num)):
    if num[i-1] == num[i]:
        continue
    else:
        x += 1
print(x//2)


