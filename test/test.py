a = set([1,2,3,4])
b = set([3,4,5,6])
print(a.intersection(b))

def sum_ab(a,b):
    for i in range(5):
        yield (a,b)
        print("?!@#")
    

for i in range(1,10):
    for j in sum_ab(i,i-1):
        print(j)