a = []
def insert(data, stack):
    stack.append(data)
    return stack
def pop_data(stack):
    stack.pop()
    return stack
insert(100, a)
insert(300, a)
insert(500, a)
print("insert",a)

pop_data(a)
print("pop", a)
pop_data(a)
print("pop", a)
pop_data(a)
print("pop", a)

