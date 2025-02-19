from students import Students
from courses_crud import CRUD
from students_Crud import CRUD as crud
class Course:
    def __init__(self,name:str,students_id:list,id:int):
        self.students = []
        d = CRUD.read_all()
        x = crud.read_all()
        c = []
        s = True
        for i in d:
            if int(i['id']) == id:
                s = False
        for i in x:
            c.append(int(i['id']))
        for i in students_id:
            if i not in c:
                raise ValueError('no such student')
            self.students.append(i)
        self.name = name
        self.id = id
        if s:
            CRUD.adding_courses(self.name,self.students,self.id)
    def add_student(self,student):
        if not isinstance(student,Students):
            raise ValueError('no such student')
        self.students.append(student.id)
        CRUD.update_course(self.id,student.id)
    @staticmethod
    def authoritize(id):
        try:
            c = CRUD.read_course(id)
        except:
            raise ValueError('no such course')
        d = Course(c['name'],c['students'],c['id'])
        return d

