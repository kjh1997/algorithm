a = [0,0,1,0,1,1,0]
print(len(a)-a[::-1].index(1)-1)
print(a.count())