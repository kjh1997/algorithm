a = {"a":1}
a["b"] =2
a["c"] =3

zip_data = zip(a.values() , a.keys())
print(zip_data)
b = {}
for i in zip_data:
    b[i[0]]   = i[1]
print(b) 