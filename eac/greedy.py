# 입력 0 < x < 10000 
# 동전으로 환전
# 1의 자리는 존재하지 않음.
money = int(input())

def greedy(money):
    coin_list = [ 500, 100, 50, 10]
    remain = money
    data = []
    for i in coin_list:
        data.append(remain//i)
        remain -= (i * (remain//i))

    return f"500원{data[0]}개, 100원{data[1]}개, 50원{data[2]}개, 10원{data[3]}개"
print(greedy(money))    