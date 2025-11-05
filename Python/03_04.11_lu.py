# # zad 1
# n1 = input("Enter num 1: ")
# n2 = input("Enter num 2: ")

# set1 = set(n1)
# set2 = set(n2)

# listBoth = list(set1.intersection(set2))
# listBoth.sort()
# print(listBoth)

# # zad 2
# m = int(input("Enter m: "))
# n = int(input("Enter n: "))
# listRange = [_ for _ in range(m, n+1)]
# result = []
# print(listRange)

# for i in listRange:
#     if (i % 3 == 0) ^ (i % 4 == 0):
#         result.append(i)

# print(result)


# # zad 3
# str = input("Enter string: ")
# letters = set(str)
# lstLetters = list(letters)
# lstLetters.sort()
# dictRes = dict()
# for i in lstLetters:
#     lst = list(str)
#     lst.remove(i)
#     dictRes[i] = lst
# print(dictRes)


# # zad 4
# str = input("Enter string: ")
# firstTuple = tuple(str)
# lst = []
# for i in range(0, len(str), 2):
#     lst.append(str[i])
# secondTuple = tuple(lst)
# print(firstTuple)
# print(secondTuple)



# # zad 5
# strInput = input("Enter list numbers separated by \", \": ")
# lst = strInput.split(", ")
# lst = [int(a) for a in lst]
# ogMax = max(lst)
# print(lst)
# while ogMax in lst:
#     lst.remove(ogMax)

# resMax = max(lst)
# indexMax = -1;
# for i in lst:
#     if i == resMax:
#         indexMax = lst.index(resMax)
#         break
    
# print(strInput)
# print(f"2nd max is {resMax}")
# print(f"Index of 2nd max is {indexMax}")



# # zad 6
# import random
 
# n = int(input("Enter n: "))
# lst = [11, 20, 19, 4, 1, 8, 4]#[random.randint(1, 21) for _ in range(n)]
# print(lst)
# evenLst = []
# for i in range(0, len(lst)):
#     if i % 2 == 0:
#         evenLst.append(lst[i])
# print(evenLst)
# evenLst.sort()
# print(evenLst)
# unevenLst = []
# for i in range(0, len(lst)):
#     if i % 2 != 0:
#         unevenLst.append(lst[i])
# unevenLst.sort()
# unevenLst.reverse()
# print(unevenLst)

# print(unevenLst + evenLst)


# zad 7
# strInput1 = input("Enter list numbers separated by \", \": ")
# lst1 = strInput1.split(", ")
# strInput2 = input("Enter list numbers separated by \", \": ")
# lst2 = strInput2.split(", ")
# result = []

# for i in range(0, len(lst1)):
#     result.append(lst1[i])
#     result.append(lst2[i])
    
# print(result)



# # zad 8 
# import random
# n = int(input("Enter n: "))
# for i in range(0, n):
#     for i in range(0, n):
#         print(random.randint(1, 17), end=" ")
#     print()
    


# zad 9
word = "мишка"
attempts = 0
length = len(word)
letters = list(word)
guessed = ['-', '-', '-', '-', '-']

for i in range(0, 5):
    print(f"Опити: {attempts}")
    print(guessed)
    
    let = input("Напиши буква: ")
    attempts += 1
    if let in letters:
        while let in letters:
            curLetters = letters
            indx = letters.index(let)
            curLetters.remove(let)
            guessed[indx] = let
            
    if '-' not in guessed:
        print(f"Браво!!! Ти успя! Думата е {word}, броят на опитите е {attempts}")
        break;
            
if '-' in guessed:
    print("Съжалявам, не позна думата !!!")
        
