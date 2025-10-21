math_students = {"Alice", "Bob", "Charlie", "David"}
science_students = {"Bob", "Eve", "Charlie", "Frank"}

print(f"math students: {math_students}")
print(f"science students: {science_students}")
print(f"Student who took both exams: {math_students.intersection(science_students)}")
print(f"Student who took at least 1 exam: {math_students.union(science_students)}")

print(f"Math students after changes: {math_students.intersection_update(science_students)}")