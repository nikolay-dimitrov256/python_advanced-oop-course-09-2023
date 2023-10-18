def students_credits(*courses):
    courses_data = {}
    result = []

    for course in courses:
        course_name, course_credits, max_points, diyans_points = course.split('-')
        course_credits, max_points, diyans_points = int(course_credits), int(max_points), int(diyans_points)
        current_points = diyans_points / max_points * course_credits

        courses_data[course_name] = current_points

    total_credits = sum(courses_data.values())

    if total_credits >= 240:
        result.append(f'Diyan gets a diploma with {total_credits:.1f} credits.')
    else:
        credits_needed = 240 - total_credits
        result.append(f'Diyan needs {credits_needed:.1f} credits more for a diploma.')

    courses_data = sorted(courses_data.items(), key=lambda kvp: -kvp[1])

    for name, current_credits in courses_data:
        result.append(f'{name} - {current_credits:.1f}')

    return '\n'.join(result)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)
print()
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
print()
print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
