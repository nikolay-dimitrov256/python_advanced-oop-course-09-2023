def gather_credits(needed_credits: int, *args):
    collected_credits = 0
    signed_courses = set()
    result = ''

    for course, current_credits in args:
        if collected_credits >= needed_credits:
            break

        if course in signed_courses:
            continue

        collected_credits += current_credits
        signed_courses.add(course)

    if collected_credits >= needed_credits:
        result = (f'Enrollment finished! Maximum credits: {collected_credits}.'
                  f'\nCourses: {", ".join(sorted(signed_courses))}')
    else:
        result = (f'You need to enroll in more courses! You have to gather '
                  f'{needed_credits - collected_credits} credits more.')

    return result


print(gather_credits(
    80,
    ("Basics", 27),
))
print()
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
print()
print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))
