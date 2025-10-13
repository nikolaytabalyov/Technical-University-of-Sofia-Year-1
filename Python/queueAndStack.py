from collections import deque
import random

dq = [random.randint(-100,100) for i in range(10)]
print(dq)

dq = deque()

dq.append(-111)
print(dq)
dq.popleft()
print(dq)

dq.append(-222)
print(dq)
dq.pop()
print(dq)

# tuple
t = ()
t = (1,2,3,4,5)
print(t)
x1,x2,x3,x4,x5 = t
print(x1,x2,x3,x4,x5)
t = (1,)
print(type(t), t)
t = 1
print(type(t), t)
