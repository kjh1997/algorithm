import base64
for i in range(int(input())):print(f'{i} {base64.b64decode(input()).decode("UTF-8")}')
