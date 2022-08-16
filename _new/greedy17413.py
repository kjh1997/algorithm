indata = input()
data = []
while True:
    start = indata.find("<")
    end = indata.find(">")
    if start != -1 and end != -1:
        print(indata[start:end])
        
    if start ==-1 and end == -1:
        break
print(data, indata)