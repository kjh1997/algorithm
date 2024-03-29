# n = int(input())
# arr = [input()[::-1] for _ in range(n)]
# num = {} # 각 키에 수가 할당됐는지
# data ={} # 수의 위치
# num2 = [False for i in range(10)] # 숫자 n이 썼는지
# for i in range(10): #
#     data[i]=[]
# for st in arr: # 문자열 분리
#     for n,s in enumerate(st):
#         num[s]=False
#         data[n+1].append(s)
# for i in range(10):
#     if data[i] ==[]: del data[i]

# for k,v in sorted(data.items(), reverse=True):
#     for s in v:
#         for i in range(9,-1,-1):
#             if (num2[i]==False) and (num[s]==False):
#                 num2[i]=True
#                 num[s] = i
#                 break
# re = []             
# for i in arr:
#     for s in i:
#         i=i.replace(s,str(num[s]))
#     re.append(int(i[::-1]))
# print(sum(re))

import sys

n = int(sys.stdin.readline())

alpha = [] # 단어를 저장할 리스트
alpha_dict = {} # 단어 내의 알파벳별로 수를 저장할 딕셔너리
numList = [] # 수를 저장할 리스트

for i in range(n): # 단어를 입력받음
    alpha.append(sys.stdin.readline().rstrip())

for i in range(n): # 모든 단어에 대해서
    for j in range(len(alpha[i])): # 단어의 길이만큼 실행
        if alpha[i][j] in alpha_dict: # 단어의 알파벳이 이미 dict에 있으면
            alpha_dict[alpha[i][j]] += 10 ** (len(alpha[i])-j-1) # 자리에 맞게 추가 ( 1의 자리면 1 )
        else:   # 자리에 없으면 새로 추가 ( 10의 자리면 10 )
            alpha_dict[alpha[i][j]] = 10 ** (len(alpha[i])-j-1)

for val in alpha_dict.values(): # dict에 저장된 수들을 모두 리스트에 추가
    numList.append(val)

numList.sort(reverse=True) # 수들을 내림차순 정렬
sum = 0
pows = 9
for i in numList: # 첫 번째 부터 가장 큰 부분을 차지하므로 9를 곱해준다
    sum += pows * i
    pows -= 1
# 내려갈수록 그 알파벳이 차지하는 비중이 적으므로 -1 
print(sum)
