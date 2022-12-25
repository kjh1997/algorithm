for tc in range(1,11):
    input()
    data = [0]*100
    x,y=0,0
    a= [list(map(int,input().split())) for i in range(100)]
    b = max(map(sum,a))
    for i in range(100):
        x += a[i][i]
        y += a[i][99-i]
        for j in range(100): data[j] += a[i][j]
    re=max(b,x,y,max(data))
    print(f'#{tc} {re}')

# map함수 > map(사용할 함수, iterable객체)
# max함수 > max(인자들)