import json

class CRUD:
    @staticmethod
    def read_all():
        with open('students.json', 'r', encoding='utf-8') as text:
            json3 = json.load(text)

        return json3['students']
    @staticmethod
    def putting_in_students(name:str,id:int,grades:list):
        with open('students.json','r',encoding='utf-8') as text:
            json3 = json.load(text)
        json3['students'].append({'id':id,'name':name,'grades':grades})
        with open('students.json','w',encoding='utf-8') as file:
            json.dump(json3,file,indent=3)
    @staticmethod
    def taking_students_out(student_id):
        with open('students.json', 'r', encoding='utf-8') as text:
            json3 = json.load(text)
        for x,i in enumerate(json3['students']):
            if int(i['id']) == student_id:
                del json3['students'][x]
        with open('students.json', 'w', encoding='utf-8') as file:
            json.dump(json3, file, indent=3)
    @staticmethod
    def update(student_id,grade,value):
        with open('students.json', 'r', encoding='utf-8') as text:
            json3 = json.load(text)
        for x,i in enumerate(json3['students']):
            if int(i['id']) == student_id:
             #   for n,m in enumerate(i['grades']):
              #      if m == grade:
                        json3['students'][x]['grades'][grade] = value
        with open('students.json', 'w', encoding='utf-8') as file:
            json.dump(json3, file, indent=3)
    @staticmethod
    def read(student_id):
        with open('students.json', 'r', encoding='utf-8') as text:
            json3 = json.load(text)
        for i in json3['students']:
            if int(i['id']) == student_id:
                return i
  #  @staticmethod
 #   def authoritize(id):
