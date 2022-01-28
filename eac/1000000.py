T = int(input())
for k in range(T):
    result_value = 0
    max_value = []
    buy_num =  int(input())
    data = list(map(int,input().split()))
    while data != []:
        max_index = data.index(max(data))
        for i in range(max_index): result_value += (data[max_index] - data[i])
        del(data[:max_index+1])
    print(f"#{k+1} {result_value}")