h,w = map(int,input().split())
before = [list(map(int,input())) for i in range(h)]
after = [list(map(int,input())) for i in range(h)]

def change(y,x):
    for i in range(3):
        for j in range(3):
            tmp = before[y+i][x+j]
            if tmp ==0: before[y+i][x+j] =1
            else: before[y+i][x+j]=0
def check():
    for i in range(w):
        for j in range(h):
            if before[j][i] != after[j][i]:
                print(-1)
                exit()
    
cnt =0
for i in range(w-2):
    for j in range(h-2):
        if before[j][i] != after[j][i]:
            change(j,i)
            cnt +=1
check()
print(cnt)