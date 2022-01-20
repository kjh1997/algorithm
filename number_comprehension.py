for_start = input()
i=0
def pnum(num):
    a = num
    i = 0
    while (a / 1) > 10:
        a /= 10
        i +=1
    x = round(a,1)
    return x, i

while int(for_start) > i:
    input_num = int(input())
    p_num, nd = pnum(input_num)
    print(f"#{i+1} {p_num}*10^{nd}")
    i +=1



