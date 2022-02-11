f=open("CarItemBuyList_202201.txt",'r')
d=open("data.txt",'w')
cnt =0
a=[]
while True:
    data = f.readline()
    rdata = data.split(",")
    a.append(rdata[0])
    if data=='':break
    

print(len(set(a)))
for i in set(a):
    d.write(i+"\n")
print("종료")