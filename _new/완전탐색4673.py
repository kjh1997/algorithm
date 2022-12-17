data = set(range(1,10001))
newList = set()
for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    newList.add(i)
selfNum=sorted(data-newList)
for i in selfNum: print(i)