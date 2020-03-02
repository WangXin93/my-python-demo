class Instructor:
    degree = "PhD (Magic)" # class attribute
    def __init__(self, name):
        self.name = name

    def lecture(self, topic):
        print("Today we're learning about " + topic)

dumbledore = Instructor("Doumbledore")

class Student:
    instructor = dumbledore

    def __init__(self, name, ta):
        self.name = name
        self.understanding = 0
        ta.add_student(self)

    def attend_lecture(self, topic):
        Student.instructor.lecture(topic)
        if Student.instructor == dumbledore:
            print(Student.instructor.name + " is awesome!")
        else:
            print("I miss Dumbledore.")
        self.understanding += 1

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class TeachingAssistant:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student
    
    def assist(self, student):
        student.understanding += 1

snape = TeachingAssistant("Snape")
harry = Student("Harry", snape)
harry.attend_lecture("potions")

hermione = Student("Hermione", snape)
hermione.attend_lecture("herbology")

hermione.visit_office_hours(TeachingAssistant("Hagrid"))

print(harry.understanding)

print(snape.students["Hermione"].understanding)

Student.instructor = Instructor("Umbridge")
Student.attend_lecture(harry, "transfiguration")