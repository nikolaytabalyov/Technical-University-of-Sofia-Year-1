import math

# # zad 1
# m = int(input("Enter number m: "))
# n = int(input("Enter number n: "))
# result = 1

# for i in range(m, n + 1):
#     if i % 3 == 0 and i % 4 == 0:
#         result *= i
        
# print("Result is: ", result)

# # zad 2 
# count = 0
# sum = 0.00
# for i in range(7, 71):
#     if i % 3 == 0:
#         sum += i
#         count += 1
        
# print(sum / count)

# # zad 3
# n = int(input("Enter number n: "))
# if (n % 10) % 5 == 0:
#     print("Единиците на числото се дели на 5")
# else: 
#     print("Единиците на числото НЕ се дели на 5") 
# if ((n // 10) % 10) % 2 == 0:
#     print("Десетиците на числото са четни")
# else:
#     print("Десетиците на числото са Нечетни")



# # zad 4
# sum = 0

# for i in range(1, 51):
#     if (i % 2 == 0 or i % 3 == 0) and not (i % 2 == 0 and i % 3 == 0):
#         sum += i
        
# print("Sum is: ", sum)


# # zad 5 
# n = int(input("Enter number n: "))
# min = 0
# max = 0
# for i in range(n):
#     n = int(input(f"Enter number {i+1}: "))
#     if n < min or min == 0:
#         min = n
#     if n > max or max == 0:
#         max = n    
    
# print("Минималния num: ", min)
# print("Максималния num: ", max)


# # zad 6
# shapeType = input("Enter shape type (square, rectangle, right triangle): ")
# if shapeType == "square": 
#     a = int(input("Enter side a: "))
#     print(f"S = {a**2}, P = {a*4}")
# elif shapeType == "rectangle":
#     a = int(input("Enter side a: "))
#     b = int(input("Enter side b: "))
#     print(f"S = {a*b}, P = {2*a + 2*b}")
# elif shapeType == "right triangle":
#     a = int(input("Enter side a: "))
#     b = int(input("Enter side b: "))
#     print(f"S = {(a*b)/2}, P = {a + b + math.sqrt(a**2 + b**2)}")


# # zad 7
# uspeh = float(input("Въведи успех: "))
# maxStipendiq = int(input("Въведи максимална стипендия: "))

# if uspeh >= 5.50:
#     print("Стипендия: ", maxStipendiq)
# elif uspeh >= 5.00 and 5.50 > uspeh:
#     print("Стипендия: ", maxStipendiq * 0.7)       
# elif uspeh >= 4.50 and 5.00 > uspeh:
#     print("Стипендия: ", maxStipendiq * 0.5)
# elif uspeh < 4.50:
#     print("Не получава стипендия.")


# # zad 8
# gender = input("Enter gender(male/female): ")
# if gender == "male": 
#     bankAccount = int(input("Enter bank account balance: "))
#     if bankAccount >= 250000:
#         print("Подходящ кандидат")
#     else:
#         print("Неподходящ кандидат")
# elif gender == "female": 
#     chestCirc = int(input("Enter chest circumference: "))
#     if chestCirc >= 100:
#         print("Подходящ кандидат")
#     else:
#         print("Неподходящ кандидат")
    
    

# zad 9 
nToday = int(input("Enter num of today: "))    
n = int(input("Enter num of days after: "))    

for i in range(1, n+1):
    if nToday + 1 > 7:
        nToday = 1
    else:
        nToday += 1

if nToday == 1: print("понеделник")
elif nToday == 2: print("вторник")
elif nToday == 3: print("сряда")
elif nToday == 4: print("четвъртък")
elif nToday == 5: print("петък")
elif nToday == 6: print("събота")
elif nToday == 7: print("неделя")
    

    

    
        