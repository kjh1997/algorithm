T = int(input())
for k in range(T):
    start_list = []
    result_value = 0
    max_value = []
    buy_num =  int(input())
    data = list(map(int,input().split()))
    print("data", data)
    while data != []:
        print("시작")
        max_index = data.index(max(data))
        for i in range(max_index):
            result_value += (data[max_index] - data[i] )
            print(result_value)
        del(data[:max_index+1])
        print(data, result_value)
    


    print(f"#{k+1} {result_value}")