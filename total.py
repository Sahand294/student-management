from students import Students
from courses import Course
from average_grade import AVG
sahand = Students.authoritize(19)
radman = Students.authoritize(1)
math = Course.authoritize(1)
math.add_student(radman)
AVG(radman.id)
#hey man!