from itertools import permutations

k = int(input())
data = input().split()

result = []
for per in permutations([0,1,2,3,4,5,6,7,8,9],k+1) :
  tmp = True
  print(per)
  for i in range(len(data)) :
    if data[i] == '<' :
      if per[i] < per[i+1] : continue
      else : 
        tmp = False
        break
    else :
      if per[i] > per[i+1] : continue
      else : 
        tmp = False
        break
  if tmp :
    result.append(per)

print(''.join(map(str,list(max(result)))))
print(''.join(map(str,list(min(result)))))