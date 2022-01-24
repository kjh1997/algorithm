T = int(input())
for test_case in range(1, T + 1):
    width,length = map(int,input().split(" "))
    tile = []
    for i in range(width):
        tile.append(list(input("").split()))
    
    print(tile)