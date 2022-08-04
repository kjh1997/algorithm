arr = list(input())
cnt=[]
re=[]
for i in range(10):
    cnt.append(arr.count(str(i)))
cnt[6] = (cnt[6]+cnt[9])//2 if (cnt[6]+cnt[9]) % 2 ==0 else ((cnt[6]+cnt[9])//2) +1
print(max(cnt[:-1]))
