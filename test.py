# # dx = [1,0,-1,0]
# # dy = [0,1,0,-1]

# # board = [[0]*5 for i in range(5)]

# # cnt = 1
# # board[0][0]=1
# # x,y=0,0
# # while cnt !=25:
# #     for i in range(4):
# #         if cnt == 25: break
# #         for _ in range(10000000):
# #             if 0<= x+dx[i] < 5 and 0<= y+dy[i] < 5 and board[x+dx[i]][y+dy[i]] == 0:
# #                 x= x+dx[i]
# #                 y = y +dy[i]
# #                 board[x][y]= cnt+1
# #                 cnt +=1
# #               #  print(x,y)
# #             else: break

# # re = 0
# # for i in range(5):
# #     re += board[i][i]
# # print(re)
# # fees = [180, 5000, 10, 600]
# # recoeds = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", 
# # "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", 
# # "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

# from heapq import heappush, heappop,heapify
# from multiprocessing import heap
# data = []
# heappush(data, 10)
# heappush(data, 310)
# heappush(data, 1)
# heappush(data, 102)
# heappush(data, 15)
# print(data)
# print(heappop(data))
# print(heappop(data))
# print(heappop(data))
# print(heappop(data))
# print(heappop(data))

def solution(grid):
    answer = 0
    for i in range(4):
        for j in range(4):
            for k in range(j + 1, 4, 2):
                answer = max(answer, max(grid[i][j] + grid[i][k], grid[j][i] + grid[k][i]))
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
grid = [[1, 4, 16, 1], [20, 5, 15, 8], [6, 13, 36, 14], [20, 7, 19, 15]]
ret = solution(grid)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")