data =set()
t = [[1,1],[2,2],[2,1],[1,5]]
t = sorted(t,key=lambda x : (x[0],x[1]))

data.add(str([1,2,3]))
data.add(str(t))

print(data)