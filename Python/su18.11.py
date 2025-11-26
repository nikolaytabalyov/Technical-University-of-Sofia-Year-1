# zad 1

# team1_counter = 0
# team2_counter = 0

# winners = input("Enter winners, separated by space: ").split(" ")
# for winner in winners:
#     if winner == "Team1": team1_counter += 1
#     elif winner == "Team2": team2_counter += 1

# if team1_counter > team2_counter:
#     print("Team 1 won")
# elif team2_counter > team1_counter:
#     print("Team 2 won")
# else:
#     print("Tie")


# # zad 2
# def checkPerfectNum(num):
#     divisors_sum = 0
#     for i in range(1, num):
#         if num % i == 0:
#             divisors_sum += i
#     return divisors_sum == num

# number = int(input("Enter a number: "))
# if checkPerfectNum(number):
#     print(f"{number} is a perfect number.") 
# else:
#     print(f"{number} is not a perfect number.")



# zad 3
# def binaryToDecimal(binary_string):
#     decimal_value = 0
#     binary_length = len(binary_string)
#     for i in range(binary_length):
#         bit = int(binary_string[binary_length - 1 - i])
#         decimal_value += bit * (2 ** i)
#     return decimal_value

# binary_input = input("Enter a binary number: ")
# decimal_output = binaryToDecimal(binary_input)
# print(f"The decimal of {binary_input} is {decimal_output}.")



# zad 4
# def decimalToBinary(decimal_number):
#     if decimal_number == 0:
#         return "0"
#     binary_string = ""
#     while decimal_number > 0:
#         remainder = decimal_number % 2
#         binary_string = str(remainder) + binary_string
#         decimal_number = decimal_number // 2
#     return binary_string

# decimal_input = int(input("Enter a decimal number: "))
# binary_output = decimalToBinary(decimal_input)
# print(f"The binary of {decimal_input} is {binary_output}.")



# # zad 5
# def sum_pair_in_lists(list1, list2):
#     summed_list = []
#     if len(list1) > len(list2):
#         j = 0
#         for i in range(len(list1)):
#             if j < len(list2):
#                 summed_list.append(list1[i] + list2[j])
#                 j += 1
#             else: 
#                 j = 0
#                 summed_list.append(list1[i] + list2[j])
#                 j += 1
#     elif len(list1) < len(list2):
#         j = 0
#         for i in range(len(list2)):
#             if j < len(list1):
#                 summed_list.append(list1[j] + list2[i])
#                 j += 1
#             else: 
#                 j = 0
#                 summed_list.append(list1[i] + list2[j])
#     else:
#         for i in range(len(list1)):
#             summed_list.append(list1[i] + list2[i])
            
#     return summed_list

# list1 = [1, 2, 3, 4, 5, 6, 7]
# list2 = [10, 20, 30]
# result = sum_pair_in_lists(list1, list2)
# print("Summed List:", result)




# # zad 6
# def get_avg_min_max(numbers):
#     total = sum(numbers)
#     avg = total / len(numbers)
#     minimum = min(numbers)
#     maximum = max(numbers)
#     return avg, minimum, maximum

# numbers = [10, 5, 8, 20, 15]
# avg, minimum, maximum = get_avg_min_max(numbers)
# print(f"Average: {avg}, Minimum: {minimum}, Maximum: {maximum}")



# # zad 7
# def make_str(str, indexes):
#     result = ""
#     for i in range(len(str)):
#         if i in indexes:
#             result += str[i]
#     return result

# input_str = "abcdefghij"
# input_indexes = [0, 2, 4, 6, 8]
# output_str = make_str(input_str, input_indexes)
# print(output_str)


# # zad 8
# import math

# def least_common_multiple(num1, num2):
#     gcd = math.gcd(num1, num2)
#     lcm = abs(num1 * num2) // gcd
#     return lcm
            
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# result = least_common_multiple(num1, num2)
# print(f"The least common multiple of {num1} and {num2} is {result}.")        



# # zad 9

# import random


# def form_matrix(rows, cols):
#     matrix = []
#     for i in range(rows):
#         row = []
#         for j in range(cols):
#             value = random.randint(1, 10)
#             row.append(value)
#         matrix.append(row)
#     return matrix

# def print_matrix(matrix):
#     for row in matrix:
#         print(" ".join(str(x) for x in row))
        
# def sum_cols(matrix):
#     cols = len(matrix[0])
#     col_sums = [0] * cols
#     for row in matrix:
#         for j in range(cols):
#             col_sums[j] += row[j]
#     return col_sums
        
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))
# matrix = form_matrix(rows, cols)
# print("Generated Matrix:")
# print_matrix(matrix)
# col_sums = sum_cols(matrix)
# for sum in col_sums:
#     print(sum, end=" ")    




# zad 10
# def CheckPrime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def CheckCanBeExpressedAsSumOfTwoPrimes(num):
#     for i in range(2, num):
#         if CheckPrime(i) and CheckPrime(num - i):
#             return True
#     return False

# number = int(input("Enter a number: "))
# if CheckCanBeExpressedAsSumOfTwoPrimes(number):
#     print(f"{number} can be expressed as the sum of two prime numbers")
# else:
#     print(f"{number} cannot be expressed as the sum of two prime numbers")