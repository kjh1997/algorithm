# FIFO 
a = []
def insert(data, queue):
    queue.append(data)
    return queue
def pop(queue):
    data = queue.pop()
    return data, queue

insert(10, a)
insert({"a":123}, a)
insert(40, a)
insert(100, a)
print("insert", a)
pop(a)
print("pop", a)