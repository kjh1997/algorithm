a = [1, [2], [3]]
import copy
b = copy.deepcopy(a)
c = copy.copy(a)
d= a
print("a", a)
print("b", b)
print("c", c)
print("d", d)
a[2].append(5)
b[1].append(5)
a.append(75)
c.append(55)
b[2].append(15)

print("a base", a)
print("b deep", b)
print("c copy", c)
print("d -- =", d)

