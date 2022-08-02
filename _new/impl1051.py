h,w=map(int,input().split())
map = [list(map(int,input())) for i in range(h)]
result = 0

for i in range(h-1):
    for j in range(w-1):
        for k in range(1,min(h-i,w-j)):
            d = map[i][j]
            if map[i+k][j] == d and map[i][j+k] == d and map[i+k][j+k] == d:
                result = max((k+1)**2, result)
print(result if result != 0 else 1)




