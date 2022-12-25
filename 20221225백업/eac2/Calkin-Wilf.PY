T = int(input())
for TC in range(1, T + 1):
    R,L = 1,1
    for i in input():
        if i =="R": R+=L
        elif i =="L": L+=R
    print(f'#{TC} {R} {L}')
