import random

l = []

# for i in range(5):
#     x = int(input(f"{i+1}: "))
#     l.append(x)
    
# print(l)

# l = []

# for i in range(5):
#     l.append(random.randint(-10, 10))
    
# print(l)

# sum = 0
# for i in range(len(l)):
#     sum += l[i]
    
# print(f"Sum = {sum}")

# sum = 0
# for i in l:
#     sum += i

# print(f"Sum = {sum}")

# stringInput = "10,11,12,14,15"
# ll = stringInput.split(",")
    
# for x in ll:
#     for y in x:
#         print(y,end=" ")
#     print()

l = []
for i in range(8):
    l.append(random.randint(-10, 10))

# slices

# print(l)
# print(l[1:3])
# print(l[1:])
# print(l[:4])
# print(l[-2:])
# print(l[:-3])
# print(l[-4:-2])

# del 

print(l)
del l[5]
print(l)
del l[1:5]
print(l)