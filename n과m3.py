# import sys
# n,m = map(int,sys.stdin.readline().split())

# arr = []
# def sol():
#     if len(arr) == m: print(*arr); return
#     for i in range(1, n+1):
#         arr.append(i)
#         sol()
#         arr.pop()
# sol()