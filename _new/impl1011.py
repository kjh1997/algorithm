n = int(input())
for _ in range(n):
    x,y = map(int,input().split())
    d = y-x
    print(int(((4*d)-1)**(0.5)))

