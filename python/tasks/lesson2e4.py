data = {
  "studenter": [
    ("Alice", {"ålder": 25, "ämnen": ("Matematik", "Fysik"), "aktiv": True}),
    ("Bob", {"ålder": 22, "ämnen": ("Biologi",), "aktiv": False}),
    ("Charlie", {"ålder": 23, "ämnen": ("Matematik", "Biologi"), "aktiv": True}),
    ("Diana", {"ålder": 24, "ämnen": ("Fysik",), "aktiv": False}),
    ("Eve", {"ålder": 21, "ämnen": ("Matematik", "Fysik", "Biologi"), "aktiv":
      True}),
  ],
  "kurser": {
    "Matematik": {"studenter": {"Alice", "Charlie", "Eve"}},
    "Fysik": {"studenter": {"Alice", "Diana", "Eve"}},
    "Biologi": {"studenter": {"Bob", "Charlie", "Eve"}},
  }
}

## Without ifs and loops (still as method built-ins though)

active_students = tuple(map(lambda student: student[0], filter(lambda student: student[1]["aktiv"], data["studenter"])))
unique_courses_active = set(filter(lambda course: course[0], data["kurser"]))

# Lambda function to get active students for a given course
get_active_students_for_course = lambda course_data: set(filter(lambda student: student in course_data["studenter"], active_students))

# Construct dictionary with key|value
active_students_per_course = dict(map(lambda course: (course, len(get_active_students_for_course(data["kurser"][course]))), unique_courses_active))

print(active_students)
print(unique_courses_active)
print(active_students_per_course)