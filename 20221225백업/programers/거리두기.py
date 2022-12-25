from collections import deque
dx = [-1,1,0]
dy = [0,0,1]

def solution(map):
    answer = []
    for i in map:
        arr = []
        for j in i:
            arr.append(list(j))
        answer.append(getAnswer(arr))
    return answer
def getAnswer(arr):
    print(arr)
    for x in range(5):
        for y in range(5):
            if arr[y][x] =="P":
                if check(y,x,arr) == 0: 
                    return 0
    return 1
def check(x,y,arr):
    q = deque()
    q.append((y,x,0))
    visit = [[0]*5 for i in range(5)]
    while q:
        data = q.popleft()
        if visit[data[1]][data[0]] == 1: continue
        visit[data[1]][data[0]]=1
        if data[2]==3:print("data[2]==3",data[1],data[0],arr[data[1]][data[0]], data[2]); return 1
        if arr[data[1]][data[0]] == "X": continue
        if arr[data[1]][data[0]] =="P" and data[2]!=0:print("arr[data[1]][data[0]] ==P ",data[1],data[0],arr[data[1]][data[0]], data[2]); return 0
        for i in range(3):
            ny = data[0]+dy[i]
            nx = data[1]+dx[i]
            if 0>ny or ny >=5 or 0>nx or nx >=5: continue
            q.append([ny,nx,data[2]+1])

    return 1











print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))