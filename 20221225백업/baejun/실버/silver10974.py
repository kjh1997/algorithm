from itertools import permutations, combinations
pool=[str(i) for i in range(1,int(input())+1)]
for i in list(map(' '.join, permutations(pool))):
    print(i)
# a = [i for i in range(1,int(input())+1)]
# l=len(a)

# def perm(idx=0):
#     if idx==l:
#         print(" ".join(list(map(str,a))))
#     else:
#         for i in range(idx, l):
#             a[idx],a[i] = a[i],a[idx]
#             perm(idx+1)
#             a[i],a[idx] = a[idx],a[i]
# perm(0)