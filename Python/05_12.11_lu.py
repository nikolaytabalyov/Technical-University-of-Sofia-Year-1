# class MyFirstClass:
#     x = 5

# print(MyFirstClass.x)

# MyFirstObject = MyFirstClass()

# print(MyFirstObject.x)

# # ---

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# MyPerson = Person("Ivan", 35)

# print(MyPerson.name)
# print(MyPerson.age)

# # ---

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.__w = 10

# # ---

# class Car:
#     car_type = "sports"
#     def __init__(self, color):
#         self.__color = color
    
#     def print_car(self):
#         print(self.__color, "\t", self.car_type)
    
#     def get_color(self):
#         return self.__color
    
#     def set_color(self, color):
#         self.__color = color

# car2 = Car("yellow")
# car2.print_car()

# car2.color = "black"
# car2.print_car()

# # print(car2.__color)
# print(car2.get_color())

# car2.set_color("green")
# print(car2.get_color())
# car2.print_car()

# # ---

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def greetings(self):
#         print("Hello, my name is " + self.name)

# MyPerson = Person("Ivan", 35)
# MyPerson.greetings()

# # ---

# class FirstClass:
#     x = 5
#     def FirstClassMethod():
#         print("This is class method")

# FirstClass.FirstClassMethod()

# # ---

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# Myperson = Person("Ivan", 40)
# Myperson.age = 41
# print(Myperson.age)

# # ---

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# MyPerson = Person("Ivan", 35)
# print(MyPerson.age)
# del MyPerson.age
# # print(MyPerson.age)

# # ---

# class Person:
#     def __init__(self, name):
#         self.name = name

# MyPerson = Person("Ivan")
# print(MyPerson.name)
# del MyPerson
# # print(MyPerson)

# # ---

# class Person:
#     pass

# # ---

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printname(self):
#         print(self.firstname, self.lastname)

# p = Person("Ivan", "Ivanov")
# p.printname()

# MyPerson = Person("Ivan", "Petrov")
# MyPerson.printname()

# # ---

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     pass

# MyStudent = Student("Petar", "Vasilev")
# MyStudent.printname()

# # ---

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname):
#         Person.__init__(self, fname, lname)

# s = Student("Petar", "Vasilev")
# s.printname()

# # ---

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)

# s = Student("Petar", "Vasilev")
# s.printname()

# # ---

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname, graduationyear):
#         super().__init__(fname, lname)
#         self.graduationyear = 2019

# MyStudent = Student("Petar", "Vasilev", 2019)
# MyStudent.printname()
# print(MyStudent.graduationyear)

# # ---

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year

# MyStudent = Student("Petar", "Vasilev", 2019)
# MyStudent.printname()
# print(MyStudent.graduationyear)

# # ---

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year
    
#     def  welcome (self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# MyStudent = Student("Petar", "Vasilev", 2019)
# MyStudent.printname()
# print(MyStudent.graduationyear)
# MyStudent.welcome()

# # ---

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
    
#     def __str__(self):
#         return f"{self.firstname} {self.lastname}"

# person1 = Person("Polina", "Koleva")
# print(person1)

# # ---

# # Решение на Задача 1
# class Person:
#     def __init__(self, name, family, age, nationality):
#         self.name = name
#         self.family = family
#         self.age = age
#         self.nationality = nationality
    
#     def print_info(self):
#         print(f"Име: {self.name} {self.family}, Националност: {self.nationality}")

# person1 = Person("Ivan", "Ivanov", 35, "Bulgarian")
# person2 = Person("Maria", "Petrova", 28, "Bulgarian")

# person1.print_info()
# person2.print_info()

# # ---

# # Решение на Задача 2
# class Person:
#     def __init__(self, name, family, age, nationality):
#         self.name = name
#         self.family = family
#         self.age = age
#         self.nationality = nationality
    
#     def print_info(self):
#         print(f"Име: {self.name} {self.family}, Националност: {self.nationality}")

# class Student(Person):
#     def __init__(self, name, family, age, nationality, university, yearofstudy):
#         super().__init__(name, family, age, nationality)
#         self.university = university
#         self.yearofstudy = yearofstudy
    
#     def print_info(self):
#         super().print_info()
#         print(f"Университет: {self.university}, Година на обучение: {self.yearofstudy}")

# student1 = Student("Petar", "Vasilev", 20, "Bulgarian", "TU-Sofia", 3)
# student2 = Student("Elena", "Georgieva", 21, "Bulgarian", "SU", 4)

# student1.print_info()
# student2.print_info()

# # ---

# # Решение на Задача 3
# class Person:
#     def __init__(self, name, family, age, nationality):
#         self.name = name
#         self.family = family
#         self.age = age
#         self.nationality = nationality
    
#     def print_info(self):
#         print(f"Име: {self.name} {self.family}, Националност: {self.nationality}")

# class Student(Person):
#     def __init__(self, name, family, age, nationality, university, yearofstudy):
#         super().__init__(name, family, age, nationality)
#         self.university = university
#         self.yearofstudy = yearofstudy
    
#     def print_info(self):
#         super().print_info()
#         print(f"Университет: {self.university}, Година на обучение: {self.yearofstudy}")

# class Lecturer(Person):
#     def __init__(self, name, family, age, nationality, university, experience):
#         super().__init__(name, family, age, nationality)
#         self.university = university
#         self.experience = experience
    
#     def print_info(self):
#         super().print_info()
#         print(f"Университет: {self.university}, Опит: {self.experience} години")

# lecturer1 = Lecturer("Georgi", "Dimitrov", 45, "Bulgarian", "TU-Sofia", 15)
# lecturer2 = Lecturer("Ana", "Stoyanova", 38, "Bulgarian", "UNWE", 8)

# lecturer1.print_info()
# lecturer2.print_info()



# zadacha 1

class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality
    
    def print_info(self):
        print(f"Име: {self.name} {self.family}, Националност: {self.nationality}")

print("Person info:")
person = Person("Ivan", "Ivanov", 35, "Bulgarian")
person.print_info()
        
# zadacha 2

class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy
    
    def print_info(self):
        super().print_info()
        print(f"Университет: {self.university}, Година на обучение: {self.yearofstudy}")
        
print("Student info:")
student = Student("Petar", "Vasilev", 20, "Bulgarian", "TU-Sofia", 3)
student.print_info()
        
# zadacha 3

class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience
    
    def print_info(self):
        super().print_info()
        print(f"Университет: {self.university}, Опит: {self.experience} години")

print("Lecturer info:")
lecturer = Lecturer("Georgi", "Dimitrov", 45, "Bulgarian", "TU-Sofia", 15)
lecturer.print_info()