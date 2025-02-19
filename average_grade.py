import sqlite3
from students_Crud import CRUD
class AVG:
    @staticmethod
    def check_student_id(id):
        c = CRUD.read_all()
        h = []
        for i in c:
            h.append(i['id'])
        if id not in h:
            raise ValueError('no such student')
    @staticmethod
    def avg(grades:list):
        grade = 0
        gradess = 0
        number = 0
        for i in grades:
            number += 1
            grade += int(i)
        gradess = grade/number
        return gradess
    def __init__(self,student_id):
        self.check_student_id(student_id)
        y = CRUD.read(student_id)
        grades = y['grades'].values()
        avg = self.avg(grades)
        self.add_the_grade(student_id,avg)
    @staticmethod
    def update(student_id):
        AVG.check_student_id(student_id)
        AVG.destroy_grade(student_id)
        AVG(student_id)
    @staticmethod
    def add_the_grade(student_id,grade):
        connection = sqlite3.connect('avg.db')
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO students_Avg VALUES ({student_id},{grade})")
        connection.commit()
        connection.close()
    @staticmethod
    def destroy_grade(student_id):
        connection = sqlite3.connect('avg.db')
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM students_Avg WHERE student_id = {student_id}")
        connection.commit()
        connection.close()