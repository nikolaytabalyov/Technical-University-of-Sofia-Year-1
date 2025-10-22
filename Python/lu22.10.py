# s = [1, 3, 5, 7]
# print(s[1])
# s[1] = 11
# print(s)

# s = list()
# s1 = list('Python')
# print(s1)

# s = ['P', 'Y', 'T', 'H', 'O', 'N', 3]

# s = []
# s.append(5)
# s.append(10)
# s.append(20)
# print(s)

# A=list( k for k in range(1,21) if k%3!=0)
# print(A)

# s = [2, 4, 6, 8]
# s[0] = 7
# print(s[0])

# s = [1, 2, 3, 4, 5, 6]
# print(s[::-1])
# print(s[:-1])
# print(s[1:])
# print(s[0:2])
# print(s[-1:])

# s = [1, 2, 3, 4, 5, 6]
# s1 = [9, 8]
# s2 = s +s1
# print(s2)

# s = [[1, 2, 3, 4], ['a', 'b', 'c'], [10, 20]]
# print(s[0][3])
# print(s[2][0])

# s = [1, 2, 3, 4, 5, 6]
# for i in s:
#     print(i, end=' ')

# s = [1, 2, 3, 4, 5, 6]
# for i in range(len(s)):
#     print(s[i], end=' ')

# s = [2, 4, 6, 8]
# print(4 in s)

# s = [2, 4, 6, 8, 2]
# print(s.count(2))
# print(s.index(3))
# print(min(s))
# print(max(s))

# s = [2, 4, 6, 8, 2]
# s.append(22)
# print(s)
# s += [44, 88]
# print(s)
# s.insert(0, 90)
# print(s)
# s.pop(0)
# print(s)
# s.remove(2)
# print(s)
# del s[4]
# print(s)

# import random
# s = [2, 4, 6, 8, 2]
# random.shuffle(s)
# print(s)
# print(random.choice(s))
# s.reverse()
# print(s)

# s = [45, 10, 55, 5, 35]
# s.sort()
# print(s)
# s.sort(reverse=True)
# print(s)

# s1 = ['s', 'T', 'a', 'E', 'f']
# s1.sort(key=str.lower)
# s1.sort()
# print(s1)

# k = (7, 5, 3)
# print(k)

# tup = tuple([10, 20, 30])
# print(tup)
# tup1 = tuple('python')
# print(tup1)
# tup2 = tuple()
# print(tup1)

# k = (7, 5, 3, 6, 1)
# print(k[0])
# print(k[2:3])
# print(7 in k)
# print(k * 3)
# tup = k + (2, 4)
# print(tup)

# tup = (7, 5, 3, 6, 1)
# tup.index(1)
# print(tup.index(1))
# tup.count(5)
# print(tup.count(5))

# for i in tup:
#     print(i, end=' ')

# d1 = dict(name='ivan', last_name='petrov')
# d3 = dict([ ('name', 'polina'), ('l_name', 'koleva')])
# print(d3)
# print(d1)

# d = { }
# d['name'] = 'petyr'
# d['l_name'] = 'kolev'

# d = {'name': 'ivan', 'last_name': 'ivanov'}
# print(d)

# d = {'name': 'ivan', 'last_name': 'ivanov'}
# # print(d['fname']) # Този ред е оставен като пример за KeyError, но е закоментиран, за да може кодът да се изпълни без грешка.

# b = 'fname' in d
# print(b )

# d = {'name': 'ivan', 'last_name': 'ivanov'}
# len(d)
# print(len(d))

# d['s_name'] = 'petrov'
# print(d)

# del d['s_name']
# print(d)

# d = {"name": "ivan", "last_name": "ivanov"}
# for key in d.keys():
#     print("({0} => {1})".format(key, d[key]), end=' ')

# d = {"name": "ivan", "last_name": "ivanov"}
# keys = list(d.keys())
# keys.sort()
# for key in keys:
#     print("{0} => {1} ".format(key, d[key]), end=' ')
#     print(f"{key} => {d[key]}", end=' ')

# s = set([1, 2, 3, 1])
# print(s)
# s2 = set("hello")

# s2 = set("hello")
# for i in s2:
#     print(i, end=' ')

# print(len(s2))

# s = set([1, 2, 3])
# s1 = set([4, 2, 6])
# s3 = s | s1
# print(s3)

# s = set([1, 2, 3, 4])
# s1 = set([2, 4, 6])
# s2 = s - s1
# s3 = s1 - s

# s = set([1, 2, 3, 4])
# s1 = set([2, 4, 6])
# s4 = s & s1

# s = set([1, 2, 3, 4])
# s1 = set([2, 4, 6])
# s5 = s ^ s1

# s1 = set([2, 4, 6])
# s1.add(8)
# s1.remove(2)
# print(s1)
# # s1.remove(2) # Този ред е оставен като пример за KeyError, но е закоментиран, за да може кодът да се изпълни без грешка.

# print("Hello")
# print('Hello')
# print('Hello, " World " ')
# print("hello","world")

# S=""" hello ,
# *****
# World!!! """

# S="123"
# print(S[0])
# s1="Hello"
# s1[:]
# s1[:-1:]
# s1[1::2]
# s1[1::]

# print("Hello"+"world")

# "hell" in "Hello"
# "hell" in "hello"

# print("f" * 5)


# zad 1
import random


# n = input("Enter number n: ")
# lofNs = []
# revList = []
# for i in range(len(n)):
#     lofNs.append(int(n[i]))
# tupOrdinary = tuple(n for n in lofNs)
# lofNs.reverse()
# tupNonordinary = tuple(n for n in lofNs)
# print(tupOrdinary)
# print(tupNonordinary)

# zad 2
n = int(input("Enter length of list: "))
l = list(random.randint(1, 10) for _ in range(n))
modded_list = []
for i in range(len(l) - 1):
    modded_list.append(l[i])
    modded_list.append(l[i] + l[i + 1])
    
modded_list.append(l[len(l) - 1])
print(l)
print(modded_list)

