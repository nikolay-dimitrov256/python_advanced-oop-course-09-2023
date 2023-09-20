students_count = int(input())

students = {}

for _ in range(students_count):
    name, grade = input().split()

    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for key, value in students.items():
    grades = " ".join([f'{num:.2f}' for num in value])
    print(f'{key} -> {grades} (avg: {sum(value) / len(value):.2f})')
