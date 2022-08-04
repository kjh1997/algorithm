while True:
    s = input()
    if s =="0": break
    print("yes" if s[::-1] == s else "no")