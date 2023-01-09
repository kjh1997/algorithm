import sys
input = sys.stdin.readline
data = [list(input().strip()) for i in range(5)]

dx,dy = [0,0,1,-1],[1,-1,0,0]
visit=[[False]*5 for i in range(5)]
res = set()   
def start(lis,s,y):
    if len(lis)==7:
        if s>=4:
            lis.sort()
            res.add(str(lis))
        return
    for li in lis:
        for i in range(4):
            cx = li[0]+dx[i]
            cy = li[1]+dy[i]
            if 0<= cx < 5 and 0<=cy <5 and visit[cx][cy] == False:
                if data[cx][cy] == "S" :
                    visit[cx][cy] = True
                    start(lis +[(cx,cy)],s+1,y)
                    visit[cx][cy] = False
                elif y+1<4:
                    visit[cx][cy] = True
                    start(lis +[(cx,cy)],s,y+1)
                    visit[cx][cy] = False
    
for i in range(5):
    for j in range(5):
        if data[i][j] == "S":
            visit[i][j] = True
            start([(i,j)],1,0)
            visit[i][j] = False
print(len(res))