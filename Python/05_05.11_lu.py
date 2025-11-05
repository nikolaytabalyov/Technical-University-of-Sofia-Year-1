# s = 'foobar'
# print(id(s))

# a = ['foo', 'bar', 'baz', 'qux']
# print(len(a)) # 4

# print(any([False, False, False])) # False
# print(any([False, True, False]))
# # True
# print(any(['bar' == 'baz', len('foo') == 4, 'qux' in {'foo', 'bar', 'baz'}]))
# # False

# print(any(['bar' == 'baz', len('foo') == 3, 'qux' in {'foo', 'bar', 'baz'}]))
# # True

# def f():
#     s = 'Inside f()'
#     print(s)
# print('Before calling f()')
# f()
# print('After calling f()')

# def f(qty, item, price):
#     print(f'{qty} {item} cost ${price:.2f}')
# f(6, 'bananas', 1.74) #6 bananas cost $1.74

# # Too few arguments - Uncomment to see the error
# # f(6, 'bananas')

# # Too many arguments - Uncomment to see the error
# # f(6, 'bananas', 1.74, 'pears')

# f(6, 'bananas', 1.74) # правилно

# # Извикване с аргументи-ключови думи
# f(qty=6, item='bananas', price=1.74) #-> 6 bananas cost $1.74

# # Грешка: Неочакван аргумент-ключова дума - Uncomment to see the error
# # f(qty=6, item='bananas', cost=1.74)

# def f(qty=6, item='bananas', price=1.74):
#     print(f'{qty} {item} cost ${price:.2f}')

# f(4, 'apples', 2.24) # 4 apples cost $2.24
# f(4, 'apples') # 4 apples cost $1.74
# f(4) # 4 bananas cost $1.74
# f() # 6 bananas cost $1.74
# f(item='pears', qty=9) # 9 pears cost $1.74
# f(price=2.29) # 6 bananas cost $2.29

# def f_return_none():
#     print('foo')
#     print('bar')
#     return # връща None, може да се изпусне

# # Извикване за пример с return None
# f_return_none()
# # foo
# # bar

# def f_early_return(x):
#     if x < 0:
#         return
#     if x > 100:
#         return
#     print(x)

# f_early_return(-3)
# f_early_return(105)
# f_early_return(64)
# #64

# def f_error_check(error_cond1=False, error_cond2=False, error_cond3=False):
#     if error_cond1:
#         return
#     if error_cond2:
#         return
#     if error_cond3:
#         return
#     # normal processing
#     print("Нормална обработка...")

# # извикване
# f_error_check()
# # -> Нормална обработка...
# f_error_check(error_cond2=True) # -> (няма отпечатване)

# def f_return_data():
#     return 'foo'
# s = f_return_data()
# print(s) # foo

# def f_return_dict():
#     return dict(foo=1, bar=2, baz=3)
# # извикване
# print(f_return_dict())
# # -> { 'foo': 1, 'bar': 2, 'baz': 3}
# # достъп до отделен елемент
# print(f_return_dict()['baz']) # 3

# def psum(*k):
#     result = 0
#     for i in k:
#         result += i
#     return result
# s = psum(1, 2, 3, 4)
# print(s)
# # 10

# # Анонимни функции - lambda
# num = 10
# # функция на основата на ламбда израз
# L = lambda n: 2 * n + 1
# # проверка на резултат
# print('нечетни числа:')
# for k in range(num):
#     print(L(k), end=' ')

# # директно извикване на ламбда функция
# print('\n квадрати на числата:')
# for k in range(num):
#     print((lambda x: x * x)(k + 1), end=' ')

# print('\n') # Добавено за нов ред след квадратите

# # Локални и глобални променливи
# # За да работи примерът, var1 трябва да бъде декларирана глобално
# var1 = 0 # Декларираме глобалната променлива
# def func():
#     global var1
#     var1 = 10
#     print(var1) # 10

# func()



# zad 1

# def calculate_area_square(side_length):
#     return side_length * side_length

# def calculate_area_rectangle(length, width):    
#     return length * width

# def calculate_area_right_triangle(base, height):
#     return 0.5 * base * height  

# def calculate_area():
#     print("Select shape to calculate area:")    
#     print("1. Square")  
#     print("2. Rectangle")
#     print("3. Right Triangle")
#     choice = input("Enter choice (1/2/3): ")
    
#     if choice == '1':
#         side = float(input("Enter side length: "))
#         area = calculate_area_square(side)
#         print(f"Area: {area}")
#     elif choice == '2':
#         length = float(input("Enter length: "))
#         width = float(input("Enter width: "))
#         area = calculate_area_rectangle(length, width)
#         print(f"Area: {area}")
#     elif choice == '3':
#         base = float(input("Enter base: "))
#         height = float(input("Enter height: "))
#         area = calculate_area_right_triangle(base, height)
#         print(f"Area: {area}")
    
# calculate_area()



# # zad 2
# def is_number_palindrome(num):
#     str_num = str(num)
#     return str_num == str_num[::-1]

# num = int(input("Enter a number: "))
# if is_number_palindrome(num):
#     print(f"{num} is a palindrome.")
# else:
#     print(f"{num} is not a palindrome.")



# # zad 3
# def add_numbers(a, b):
#     return a + b

# def subtract_numbers(a, b): 
#     return a - b

# def multiply_numbers(a, b): 
#     return a * b    

# def divide_numbers(a, b):
#     if b != 0:
#         return a // b
#     else:
#         return "Error: Division by zero is not allowed."    
    
# def whole_number_operations(a, b):
#     print("Available operations:")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     choice = input("Select operation (1/2/3/4): ")
#     if choice == '1':
#         result = add_numbers(a, b)
#         print(f"Result: {result}")
#     elif choice == '2':
#         result = subtract_numbers(a, b)
#         print(f"Result: {result}")
#     elif choice == '3':
#         result = multiply_numbers(a, b)
#         print(f"Result: {result}")
#     elif choice == '4':
#         result = divide_numbers(a, b)
#         print(f"Result: {result}")
#     else:
#         print("Invalid choice.")
        
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# whole_number_operations(a, b)



# # zad 4
# def change_all_n_over_to_zero(lst, n):
#     for i in range(len(lst)):
#         if lst[i] > n:
#             lst[i] = 0
#     return lst

# print("Enter a list of integers separated by ', ':")
# list_input = [int(x) for x in input().split(", ")]
# n = int(input("Enter n: "))
# result = change_all_n_over_to_zero(list_input, n)
# print("Modified list:", result)