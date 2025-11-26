# # zad 1 

# class BankAccount:
#     def __init__(self, owner):
#         self.owner = owner  
#         self.__balance = 0  
#         self._transaction_history = []

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             self._transaction_history.append(f"Депозит: {amount}")
#         else:
#             print("Сума на депозита трябва да е положителна.")

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#             self._transaction_history.append(f"Теглене: {amount}")
#         else:
#             print("Недостатъчни средства.")

#     def get_balance(self):
#         return self.__balance

#     def get_transaction_history(self):
#         return self._transaction_history
    
# bankAccount = BankAccount("Иван Иванов")
# bankAccount.deposit(1000)
# bankAccount.withdraw(250)
# print("Баланс:", bankAccount.get_balance())
# print("История на транзакциите:", bankAccount.get_transaction_history())




# # zad 2
# class Student:
#     def __init__(self, name, grade, marks):
#         self.name = name
#         self.grade = grade
#         self.marks = marks
        
#     def addMark(self, mark):
#         self.marks.append(mark)
        
#     def average(self):
#         return sum(self.marks) / len(self.marks)
    
#     def info(self):
#         print(f"Студент: {self.name}, Клас: {self.grade}, Среден успех: {self.average():.2f}")

# class School:
#     def __init__(self):
#         self.students = []
        
#     def addStudent(self, student):
#         self.students.append(student)
        
#     def listStudents(self):
#         for student in self.students:
#             student.info()
            
#     def findTopStudent(self):
#         top_student = None
#         for student in self.students:
#             if top_student is None or student.average() > top_student.average():
#                 top_student = student
#         return top_student
    
# school = School()
# student1 = Student("Петър Петров", 10, [5, 6, 4])
# student2 = Student("Мария Георгиева", 11, [6, 6, 5])
# school.addStudent(student1)
# school.addStudent(student2)
# school.listStudents()
# top_student = school.findTopStudent()
# print(f"Най-добър студент: {top_student.name} със среден успех {top_student.average():.2f}")



# # zad 3
class Book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = True
        
    def print_info(self):
        return f"{self.title} от {self.author}, налична: {self.available}"
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"Вие заехте книгата: {self.title}")
        else:
            print(f"Книгата {self.title} не е налична.")
            
    def return_book(self):
        self.available = True
        print(f"Вие върнахте книгата: {self.title}")
        
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def show_available(self):
        for book in self.books:
            if book.available:
                print(book.print_info())
            
    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.available:
                    book.borrow()
                    return book
        return None
    
class EBook(Book):
    def __init__(self, title, author, file_format):
        super().__init__(title, author, True)
        self.file_format = file_format
        
    def print_info(self):
        return f"{self.title} от {self.author}, формат: {self.file_format}"
    
    
library = Library()
book1 = Book("1984", "Джордж Оруел", True)
book2 = Book("Малкият принц", "Антоан дьо Сент-Екзюпери", True)
ebook1 = EBook("Python Programming", "John Doe", "PDF")
library.add_book(book1)
library.add_book(book2)
library.add_book(ebook1)
library.show_available()
borrowed_book = library.borrow_book("1984")