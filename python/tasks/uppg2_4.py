data = {
    "studenter": [
        ("Alice", 
            {"ålder": 25,
            "ämnen": ("Matematik", "Fysik"),
            "aktiv": True}
        ),
        
        ("Bob",
            {"ålder": 22,
            "ämnen": ("Biologi",),
            "aktiv": False}
        ),
        ("Charlie",
            {"ålder": 23,
             "ämnen": ("Fysik",),
             "aktiv": False}
        ),
        ("Diana",
            {"ålder": 24,
             "ämnen": ("Fysik",),
             "aktiv": False}
        ),
        ("Eve",
            {"ålder": 21,
             "ämnen": ("Matematik", "Fysik", "Biologi"),
             "aktiv": True},
        ),
    ],
    
    "kurser": {
        "Matematik": {"studenter": {"Alice", "Charlie", "Eve"}},
        "Fysik": {"studenter": {"Alice", "Diana", "Eve"}},
        "Biologi": {"studenter": {"Bob", "Charlie", "Eve"}},
    },
}

# valde att lägga alla uppgifter i funktioner
# egentligen kan man bara köra koden direkt och ändra lite men
# detta kändes snyggast

def extractActiveStudents(data) -> tuple:
    students = data["studenter"]
    students_list = []
    # börjar med en lista istället för tuple för att kunna modifiera den
    
    for student in students:
        if student[1]["aktiv"]: # [1] specifierar ordboken, där åldern, ämnen, och aktiv finns
            students_list.append(student[0]) # lägg till deras namn, alltså [0], i listan

    return tuple(students_list)
# gör om till tuple och returnera aktiva studenter 


def extractActiveCourses(active_students: tuple, data) -> tuple:
    courses = data["kurser"]
    active_courses = []
    
    for subject in courses:
        for student_list in courses[subject].values(): # ...values() specifierar tupeln som är värdet till "studenter" för varje ämne
            for student in student_list:
                if student in active_students:
                    active_courses.append(subject)

    return tuple(set(active_courses)) 
# gör om till set för att ta bort dubletter, sedan returnera en tuple

def getActiveCourseStudents(active_students: tuple, active_courses: tuple, data) -> dict:
    courses = data["kurser"]
    active_student_in_courses = {}
    
    for subject in courses:
        if subject not in active_courses:
            continue
        # hoppa över iteration om kursen inte har aktiva studenter
        # egentligen inte nödvändigt men "best practice"
        
        for students in courses[subject].values():
            active_students_in_course = 0
            
            for student in students:
                if student in active_students:
                    active_students_in_course += 1
                    
            active_student_in_courses[subject] = active_students_in_course
            # ge varje ämne/kurs motsvarande nummer aktiva studenter
            # ex. active_student_in_courses["Matematik"] = 2
            
    return active_student_in_courses
    #returnerar som ordbok
    
#INTE DEL AV UPPGIFTEN
#gjorde endast denna för o snygga till output från print
"""def prettify(data) -> str:
    pretty_str = ""
    length = len(data)
    i = 1
    
    data_is_dict = isinstance(data, dict) 
    
    for item in data:
        if data_is_dict:
            item = f"\n{item}: {data[item]}"
        
        if i == length:
            pretty_str += f"{item} "
            break
        
        pretty_str += f"{item}, "
        i += 1
        
    return pretty_str
"""

active_students = extractActiveStudents(data)
print(f"Active students: {active_students}")

active_courses = extractActiveCourses(active_students, data)
print(f"Active courses: {active_courses}")

active_students_in_courses = getActiveCourseStudents(active_students, active_courses, data)
print(f"Active number of students, in each courses: {active_students_in_courses}")