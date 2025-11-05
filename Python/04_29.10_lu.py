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

# A = list(k for k in range(1,21) if k%3!=0)
# print(A)

# s = [1, 2, 3, 4, 5, 6]
# print(s[::-1])         # извеждаме елементите в обратен ред
# print(s[:-1])          # принтираме без последния елемент
# print(s[1:])           # принтираме без първия елемент
# print(s[0:2])          # първите два елемента
# print(s[-1:])          # последният елемент

# s = [1, 2, 3, 4, 5, 6]
# s1 = [9, 8]
# s2 = s + s1
# print(s2)

# s = [[1, 2, 3, 4], ['a', 'b', 'c'], [10, 20]]
# print(s[0][3])  # достъпваме на първия списък 4-тия елемент
# print(s[2][0])  # достъпваме на третия списък 1-вия елемент

# s = [1, 2, 3, 4, 5, 6]
# for i in s:
#     print(i, end=' ')

# s = [1, 2, 3, 4, 5, 6]
# for i in range(len(s)):
#     print(s[i], end=' ')

# s = [2, 4, 6, 8]
# print(4 in s)  # True

# s = [2, 4, 6, 8, 2]
# print(s.count(2))   # 2

# # print(s.index(3))  # ValueError: 3 is not in list

# print(min(s))   # 2
# print(max(s))   # 8

# s = [2, 4, 6, 8, 2]
# s.append(22)      # добавя в края на списъка 22
# print(s)

# s += [44, 88]     # добавя в края 44,88
# print(s)

# s.insert(0, 90)  # вмъква в началото 90
# print(s)

# s.pop(0)         # изтрива първия елемент на списъка
# print(s)

# s.remove(2)      # изтрива елемента със стойност 2
# print(s)

# del s[4]         # премахва елемента с индекс 4
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
# print(s1)

# s1 = ['s', 'T', 'a', 'E', 'f']
# s1.sort()
# print(s1)

# k = (7, 5, 3)
# print(k)

# tup = tuple([10, 20, 30])
# print(tup)

# tup1 = tuple('python')
# print(tup1)

# tup2 = tuple()
# print(tup2)

# k = (7, 5, 3, 6, 1)
# print(k[0])
# print(k[2:3])
# print(7 in k)
# print(k * 3)
# tup = k + (2, 4)
# print(tup)

# tup = (7, 5, 3, 6, 1)
# print(tup.index(1))
# print(tup.count(5))

# for i in tup:
#     print(i, end=' ')

# d = dict()
# d1 = dict(name='Ivan', last_name='Petrov')
# d3 = dict([('name', 'Polina'), ('l_name', 'Koleva')])
# print(d1)
# print(d3)

# d = {}
# d['name'] = 'Petyr'
# d['l_name'] = 'Kolev'
# print(d)

# d = {'name': 'Ivan', 'last_name': 'Ivanov'}
# print(d)

# d = {'name': 'Ivan', 'last_name': 'Ivanov'}

# # print(d['fname'])  # KeyError: 'fname'

# b = 'fname' in d
# print(b)

# d = {'name': 'Ivan', 'last_name': 'Ivanov'}
# print(len(d))

# d['s_name'] = 'Petrov'
# print(d)

# del d['s_name']
# print(d)

# d = {"name": "Ivan", "last_name": "Ivanov"}
# for key in d.keys():
#     print("({0} => {1})".format(key, d[key]), end=' ')

# d = {"name": "Ivan", "last_name": "Ivanov"}
# keys = list(d.keys())
# keys.sort()
# for key in keys:
#     print("{0} => {1} ".format(key, d[key]), end=' ')
#     print(f"{key} => {d[key]}", end=' ')

# s = set([1, 2, 3, 1])
# print(s)
# s2 = set("hello")
# print(s2)

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
# print(s2)
# s3 = s1 - s
# print(s3)

# s = set([1, 2, 3, 4])
# s1 = set([2, 4, 6])
# s4 = s & s1
# print(s4)

# s = set([1, 2, 3, 4])
# s1 = set([2, 4, 6])
# s5 = s ^ s1
# print(s5)

# s = {1, 2, 3}
# s1 = {1, 2}
# print(s1 <= s)

# s1 = set([2, 4, 6])
# s1.add(8)
# print(s1)

# s1 = set([2, 4, 6])
# s1.remove(2)
# print(s1)

# print("Hello")
# print('Hello')
# print('Hello, " World " ')
# print("hello","world")

# S = "123"
# print(S[0])

# s1 = "Hello"
# s1 = s1[:]
# print(s1)

# s1 = "Hello"
# s1 = s1[:-1:]
# print(s1)

# s1 = "Hello"
# s1 = s1[1::2]
# print(s1)

# s1 = "Hello"
# s1 = s1[1::]
# print(s1)

# print("Hello"+"world")
# print("f" * 5)

# s = "Здравей"
# print(len(s))

# print(str(123))
# s = "Hello World"
# print(repr(s))

# parts = ["apple", "banana", "cherry"]
# s = ", ".join(parts)
# print(s)

# s = "apple, banana, cherry"
# print(s.split(", "))

# s = "  hello \n"
# print(s.strip())

# print("this is a test".title())
# print("hELLo worLD".title())

# s = "banana"
# print(s.find("an"))
# print(s.find("na"))
# print(s.find("x"))

# s = "one one one"
# print(s.replace("one", "two"))

import random





# zadacha 3
# n = int(input("Enter lenght of list: "))
# a = list(random.randint(1, 9) for _ in range(n))
# b = []

# for i in range(0, len(a) - 1, 2):
#     b.append(a[i] + a[i + 1])
    
# print(a)
# print(b)


# zadacha 4
# str = input("Enter string: ")
# wordSet = set(str)
# wordDict = dict()

# for i in wordSet:
#     count = 0
#     for j in range(0, len(str)):
#         if(str[j] == i):
#             count += 1
#     wordDict[i] = count
    
# print(wordDict)


# zadacha 5
# str = input("Enter string: ")
# wordSet = set(str)
# wordDict = dict()

# for i in wordSet:
#     wordDict[i] = []
#     for j in range(0, len(str)):
#         if(str[j] == i):
#             wordDict[i].append(j)
            
# print(wordDict)

# zadacha 6
n = int(input("Enter n: "))
l = [i for i in range(1, n + 1)]
reversed = l[::-1]
dict = dict()
for i in range(0, len(l)):
    dict[i + 1] = reversed[i]
    
print(l)
print(reversed)
print(dict)