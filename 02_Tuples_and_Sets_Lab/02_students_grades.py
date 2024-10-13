number_of_students = int(input())
students_grades = {}
for _ in range(number_of_students):
    name, grade_as_string = input().split()
    grade = float(grade_as_string)

    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(grade)

for student_name, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)
    formatted_grades = f"{' '. join([f'{g:.2f}' for g in grades])}"
    print(f"{student_name} -> {formatted_grades} (avg: {average_grade:.2f})")
