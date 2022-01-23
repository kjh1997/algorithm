# S마켓에서 손님에게 거슬러 주어야 할 금액 N이 입력되면 돈의 최소 개수로 거슬러 주기 위하여 각 종류의 돈이 몇 개씩 필요한지 출력하라.
# 5만원권, 1만원권, 5천원, 1000원, 500원, 100원, 50원 
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def greedy(money):
    coin = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    remain = money
    data = ""
    for i in coin:
        data += str(remain//i) + " "
        remain -= i*(remain//i)
    return data
        
for test_case in range(1, T + 1):
    money = int(input())
    data = greedy(money)
    print(f'#{test_case} \n{data}')

