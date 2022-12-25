a = list(map(int,list(str(input()))))
a.sort(reverse=True)
print("".join(map(str,a)))