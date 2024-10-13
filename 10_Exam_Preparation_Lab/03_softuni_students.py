def softuni_students(*args, **kwargs):
    text_to_print = ""
    successfully_finished_students = {}
    invalid_course_students = []

    for student in args:
        course_id_for_user, username = student
        for course_id, course_name in kwargs.items():
            if course_id == course_id_for_user:
                if username not in successfully_finished_students:
                    successfully_finished_students[username] = []
                successfully_finished_students[username].append(course_name)
        if username not in successfully_finished_students:
            invalid_course_students.append(username)

    for user, course in sorted(successfully_finished_students.items()):
        text_to_print += f"*** A student with the username {user} " \
                         f"has successfully finished the course {str(*course)}!\n"
    if invalid_course_students:
        text_to_print += f"!!! Invalid course students: {', '.join(sorted(invalid_course_students))}"

    return text_to_print


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
