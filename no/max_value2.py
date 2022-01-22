T = int(input())
for k in range(T):
    start_list = []
    base_data = []
    result_list = []
    result_value = 0
    max_key =[]
    max_value = []
    buy_num =  int(input())
    data = input()
    data_list = data.split()
    difference_dict = {}
    for num, i in enumerate(data_list):
        difference_dict[num] = int(i)
    
    sorted_list = sorted(difference_dict.items(),key = lambda item: item[1], reverse= True)
    for num, i in enumerate(sorted_list): 
        if num == 0:
            for j in sorted_list:
                if j[0] < i[0] and j[1] < i[1]:
                    result_value += i[1] - j[1]
        else:
            
            max_key.append(sorted_list[num-1][0])
            maxkey=max(max_key)
            if i[0] < max(max_key):
                continue
            
            for j in sorted_list[num:]:

                if max(max_key) < j[0] and i[0] > j[0]:
                    result_value += (i[1] - j[1])    
              
    print(f"#{k+1} {result_value}")