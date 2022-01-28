
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
data = list(input())
result = ""
for i in data:
    result += str(a.index(i)+1) +" "
print(result)