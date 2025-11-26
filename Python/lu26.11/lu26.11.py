# zad 1

# def read_file_content(file_name):
#     try:
#         opened_file = open(file_name, 'rt')
#         content = opened_file.read()
#         opened_file.close()
#         return content
#     except FileNotFoundError:
#         return "File not found."
#     except Exception as e:
#         return f"An error occurred: {e}"

# file_name = 'lu26.11.txt'
# print(read_file_content(file_name))


# # zad 2
# import areas as ar

# input_shape = input("Enter the shape (triangle/rectangle): ").strip().lower()
# if input_shape == 'triangle':
#     print(f"The area of the triangle is: {ar.triangle_area()}")
# elif input_shape == 'rectangle':
#     print(f"The area of the rectangle is: {ar.rectangle_area()}")


# # zad 3

# import calculator as calc
# def main():
#     try:
#         num1 = int(input("Enter first integer: "))
#         num2 = int(input("Enter second integer: "))
#         operation = input("Enter operation (+, -, *, /): ")

#         if operation == '+':
#             result = calc.add(num1, num2)
#         elif operation == '-':
#             result = calc.subtract(num1, num2)
#         elif operation == '*':
#             result = calc.multiply(num1, num2)
#         elif operation == '/':
#             result = calc.divide(num1, num2)
#         else:
#             print("Invalid operation.")
#             return

#         print(f"The result of {num1} {operation} {num2} is: {result}")
#     except ValueError:
#         print("Invalid input. Please enter integers only.")
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")

# main()