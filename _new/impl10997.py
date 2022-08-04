x1,y1,x2,y2 = map(int,input().split())
x3,y3,x4,y4 = map(int,input().split())

if x1 < x3 < x2 or x1 < x4 < x2:
    if y1< y3< y2 or y1 < y4 < y2:
        print("FACE")
if x3 < x1 < x4 or x3 < x2 < x4:
    if y3< y1< y4 or y3 < y2 < y4:
        print("FACE")