def softuni_students(*args, **kwargs):
    course_students = {}
    invalid_students = set()
    result = []

    for arg in args:
        course_id, username = arg
        if course_id not in kwargs.keys():
            invalid_students.add(username)
        else:
            course_name = kwargs[course_id]
            course_students[username] = course_name

    sorted_students = sorted(course_students.items())

    for student, course_name in sorted_students:
        result.append(f"*** A student with the username {student} has successfully finished the course {course_name}!")

    if invalid_students:
        result.append(f"!!! Invalid course students: {', '.join(sorted(invalid_students))}")

    return "\n".join(result)


print(softuni_students(
    ('id_1', 'Kaloyan9905'),
    id_1='Python Web Framework',
))
print()
print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))
print()
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
