students = []


def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["name"].title())
    return students_titlecase


def print_student_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)


def add_student(name, student_id=1):
    student = {"name": name, "student_id": student_id}
    students.append(student)


def save_file(student):
    try:
        f = open("student.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("could not save file")


def read_file():
    try:
        f = open("student.txt", "r")
        for student in read_students(f):
            add_student(student)
        f.close()
    except Exception:
        print("could not read file")


def read_students(f):
    for line in f:
        yield line

# add_student(name="Kay")


def var_args(name, *args):
    print(name)
    print(args)


def var_kwargs(name, **kwargs):
    print(name)
    print(kwargs["description"], kwargs["age"], kwargs["feedback"])


# var_args("Kobby", "loves Python3", 23, None)
# var_kwargs("Kobby", description="loves Python3", age=23, feedback=None)

# student_list = get_students_titlecase()

read_file()
print_student_titlecase()


student_name = input("Enter student name: ")
student_id = input("Enter student ID: ")

add_student(student_name, student_id)
save_file(student_name)

# print_student_titlecase()
