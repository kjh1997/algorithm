r = int(input())
if r % 10 != 0: print(-1)
else:    print(r//300, (r%300)//60, ((r%300)%60)//10)

# while r!=0:
#     if r%10 != 0: print(-1); break
#     if a<=r: r-=a; d+=1
#     if b<=r: r-=b; e+=1
#     if c<=r: r-=c; f+=1
# if r == 0: print(d,e,f)
