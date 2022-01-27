T = int(input())
a = list(map(int, input().split()))
print(sorted(a)[len(a)//2])