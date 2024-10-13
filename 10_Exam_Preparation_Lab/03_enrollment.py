# def gather_credits(number_of_credits, *courses):
#     gathered_credits = 0
#     enrolled_courses = []
#     for course, credits in courses:
#         if gathered_credits < number_of_credits:
#             if course in enrolled_courses:
#                 continue
#             enrolled_courses.append(course)
#             gathered_credits += credits
#     if gathered_credits >= number_of_credits:
#         enrolled_courses = sorted(enrolled_courses)
#         return f"Enrollment finished! Maximum credits: {gathered_credits}.\n"\
#                f"Courses: {', '.join(enrolled_courses)}"
#     return f"You need to enroll in more courses! You have to gather {number_of_credits - gathered_credits} " \
#            f"credits more."
#
#
# print(gather_credits(60, ("Basics", 27), ("Fundamentals", 27), ("Advanced", 30), ("Web", 30)))

def gather_credits(max_credits, *args):
    sum_credits = 0
    courses = []

    for name_course, current_credits in args:
        if sum_credits >= max_credits:
            return f"Enrollment finished! Maximum credits: {sum_credits}.\nCourses: {', '.join(sorted(courses))}"
        if name_course not in courses:
            # continue
            courses.append(name_course)
            sum_credits += current_credits

    return f"You need to enroll in more courses! You have to gather {max_credits - sum_credits} credits more."


print(gather_credits(80, ("Advanced", 30), ("Basics", 27), ("Fundamentals", 27)))
