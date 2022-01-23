week = [1,0,0,1,0,1,0]
import time
for i in range(0,7):
    data = week[i:] +week[:i]
  
    print(data)
