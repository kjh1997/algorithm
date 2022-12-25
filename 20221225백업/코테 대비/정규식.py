d = "A man, a plan, a canal: Panama"
import re
d =re.sub('[^ㄱ-ㅎ]',"",d).strip().lower()
if d == d[::-1]:
    print(d)
    print("팔린")
print(d)