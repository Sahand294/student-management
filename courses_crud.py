import json
class CRUD:
    @staticmethod
    def update_course(id,student_id):
        with open('students.json', 'r', encoding='utf-8') as text:
            json3 = json.load(text)
        for x, i in enumerate(json3['courses']):
            if int(i['id']) == id:
                json3['courses'][x]['students'].append(student_id)
        with open('students.json', 'w', encoding='utf-8') as file:
            json.dump(json3, file, indent=3)

    @staticmethod
    def read_all():
        with open('students.json', 'r', encoding='utf-8') as text:
            json3 = json.load(text)

        return json3['courses']
    @staticmethod
    def read_course(id):
        with open('students.json', 'r', encoding='utf-8') as text:
            json3 = json.load(text)

        for i in json3['courses']:
            if int(i['id']) == id:
                return i

    @staticmethod
    def taking_course_out(name, id):
        with open('students.json', 'r', encoding='utf-8') as text:
            json3 = json.load(text)
        for x, i in enumerate(json3['students']):
            if int(i['id']) == id:
                del json3['courses'][x]
        with open('students.json', 'w', encoding='utf-8') as file:
            json.dump(json3, file, indent=3)

    @staticmethod
    def adding_courses(name, students, id):
        with open('students.json', 'r', encoding='utf-8') as text:
            json3 = json.load(text)
        json3['courses'].append({'name': name, 'students': students, 'id': id})
        with open('students.json', 'w', encoding='utf-8') as file:
            json.dump(json3, file, indent=3)