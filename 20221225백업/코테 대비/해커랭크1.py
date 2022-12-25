from collections import Counter
def birthdayCakeCandles(candles):
    result = -1
    data = Counter(candles)
    for i in data.items(): 
        result = max(i[1],result)
    return result


print(birthdayCakeCandles("3 2 1 3"))