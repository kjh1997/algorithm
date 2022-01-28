member = int(input())

people = list(map(int, input().split(" ")))
count2 = people.count(2)
count1 = people.count(1)
count3 = people.count(3)
group1, group2, group3 = count1 ,count2//2, count3//3
remain_peo1 = count2 - group2*2
remain_peo2 = count3 - group2*3
group4 = 0
if remain_peo1 == 1 and remain_peo2 == 2:
    group4 += 1 
    remain_peo2 -= 1
result = group1+ group2+ group3 + group4
print(result)