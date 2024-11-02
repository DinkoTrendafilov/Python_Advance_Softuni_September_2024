def gather_credits(needed_credits, *args):
    courses = []
    gather_credit = 0
    result = ""

    for course, credit in args:
        if gather_credit >= needed_credits:
            break
        if course in courses:
            continue

        courses.append(course)
        gather_credit += credit

    if gather_credit >= needed_credits:
        result += f"Enrollment finished! Maximum credits: {gather_credit}.\n"
        result += f"Courses: {', '.join(map(str, sorted(courses)))}"

    else:
        result += (f"You need to enroll in more courses! You have to gather"
                   f" {needed_credits - gather_credit} credits more.\n")

    return result


print(gather_credits(80, ("Basics", 27), ))
print()
print(gather_credits(80, ("Advanced", 30), ("Basics", 27), ("Fundamentals", 27), ))
print()
print(gather_credits(60, ("Basics", 27), ("Fundamentals", 27), ("Advanced", 30), ("Web", 30)))
print()
