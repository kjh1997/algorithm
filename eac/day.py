T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = list(map(int, input().split()))
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 , 31]
    result = 0

    if a[0] == a[2]:
        result = a[3] - a[1] +1 
    else:
        result = sum( day[ a[0] : a[2]-1 ] ) + day[a[0]-1] - a[1] + day[a[2] -1] - a[3] + 2
    print(result)



