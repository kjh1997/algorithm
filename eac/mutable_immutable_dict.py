import copy

a = {"3":[1,2,3]}
b = copy.copy(a)
print(id(a), id(b))
print(a, b)
print(id(a['3']), id(b['3']))
print(a['3'], b['3'])

a = {"3":[1,2,3]}
b = a
print(id(a), id(b))
print(a, b)

print(id(a['3']), id(b['3']))
print(a['3'],b['3'])

a = {"3":[1,2,3]}
b = copy.deepcopy(a)
print(id(a), id(b))
print(a, b)
print(id(a['3']), id(b['3']))
print(a['3'], b['3'])

#  dict역시 deepcopy, copy, = 의 차이가 명확하게 들어나는것을 확인 할 수 있다.
# 내부의 mutable객체까지 주소가 변화된 것을 볼 수 있다.