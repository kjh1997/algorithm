import sys
sys.setrecursionlimit(10**6)
n = int(input())

def print_star(n):
    if n == 1: return ["*"]

    star = print_star(n//3)
    p = []
    for s in star:
        p.append(s*3)
    for s in star:
        p.append(s + ' '*(n//3) + s)
    for s in star:
        p.append(s*3)
    print(p)
    return p

print("\n".join(print_star(n)))