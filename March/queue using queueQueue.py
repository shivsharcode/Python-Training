from queue import Queue

q = Queue()

q.put('A')
q.put('B')
q.put('C')

print(q)

print(q.get())
print(q.get())