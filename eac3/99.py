for tc in range(int(input())):
    a=int(input())
    cnt=0
    for i in range(1,10):
        if a//i == a/i and a//i <10: cnt=1;print(f'#{tc+1} Yes'); break
    if cnt==0:print(f'#{tc+1} No')