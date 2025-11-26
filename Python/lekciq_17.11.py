import os

def get_numbers():
    print("Enter first number in format: XXXX")
    user1_number = input()
    os.system("cls")  
    
    print("Enter second number in format: XXXX")
    user2_number = input()
    os.system("cls")  
    return user1_number, user2_number

def game():
    user1_number, user2_number = get_numbers()
    
    bulls = sum(1 for a, b in zip(user1_number, user2_number) if a == b)
    cows = sum(1 for digit in set(user1_number) if digit in user2_number) - bulls
    
    print(f"Bulls: {bulls}, Cows: {cows}")
    

game()  