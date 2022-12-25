from itertools import product
from math import prod
a = [list(input()) for i in range(5)]
data = []
result = []
for i in range(5):
    for j in range(5):
        if a[i][j] == "*": data.append((i,j))
for i in range(len(data)):
    result.append([])
    for j in range(len(data)):
        if i == j: continue
        num = 0
        if data[i][0] == data[j][0]: num +=0 
        else: num += abs(data[i][0] - data[j][0])
        if data[i][1] == data[j][1]: num +=0 
        else: num += abs(data[i][1] - data[j][1])  
        print(abs(num)) 
        result[i].append(abs(num))
# all = list(product(result[0],result[1],result[2]))
print(result)
sum_data = []

# for i in range(len(result)):
for i in range(result):
    for j in range(len(result[0])):
        