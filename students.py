from students_Crud import CRUD
class Students:
    def __init__(self,id,name,grades):
        d = CRUD.read_all()
        s = True
        self.id = id
        self.name = name
        self.grades = grades
        for i in d:
            if int(i['id']) == id:
                s = False
        if s:
            CRUD.putting_in_students(name, id, grades)


    def change_grade(self,grade,new_value):
        CRUD.update(self.id,grade,new_value)
    @staticmethod
    def authoritize(id):
        try:
            s = CRUD.read(id)
        except:
            raise ValueError('no such student')
        d = Students(s['id'],s['name'],s['grades'])
        return d