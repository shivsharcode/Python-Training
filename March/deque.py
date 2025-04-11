from collections import deque

dq = deque()

dq.append('A')
dq.append('B')

print(dq)

dq.appendleft('Z')
dq.appendleft('Y')

print(dq)

dq.pop()  # remove from right
print(dq)

dq.popleft()
print(dq)