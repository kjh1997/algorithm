T = int(input())
for test_case in range(1, T + 1):
    a=list(map(int,input().split()))
    b=sum([ i for i in a])/len(a)
    print(f'#{test_case} {round(b)}')
