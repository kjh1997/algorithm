for i in range(1, int(input())+1):
    c = sum(str(i).count(n) for n in "369")
    print("-"*c, end=" ") if c > 0 else print(i, end=" ")