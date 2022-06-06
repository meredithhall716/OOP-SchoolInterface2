from classes.staff import Staff
from classes.student import Student
from classes.person import Person

class School:
    
    def __init__(self, name):


        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        for index, for_loop_student in enumerate(Student.objects()):
            print(f'{index + 1}. {for_loop_student.name} {for_loop_student.school_id}')

    def find_student_by_id(self, school_id):
        for student in self.students:
            if student.school_id == school_id:
                return student
