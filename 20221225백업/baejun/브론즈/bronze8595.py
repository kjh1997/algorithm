import re
n = int(input())
number= list(map(int,re.findall(r'\d+',input())))
print(sum(number))
