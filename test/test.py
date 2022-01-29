visit = [0] *3
print(id(visit[0]))
print(id(visit[1]))
print(id(visit[2]))
visit[1]=2
print(visit)
print(id(visit[0]))
print(id(visit[1]))
print(id(visit[2]))