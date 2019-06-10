#__author__:Lenovo  "Yang Tian"
#date:2019/3/21

from conf import config
from dao import student

class Teacher:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.salary = 0
        self.school = school
        self.class_teacher = list()

    def set_class(self, _class):
        if _class not in self.class_teacher:
            self.class_teacher.append(_class)

    def edit_grade(self, stu, course, grade):
        for index,value in enumerate(stu.cur):
            if value["课程"].name == course.name:
                stu.cur[index]["成绩"] = grade
                return True
        return False # 课程不存在

    def show_class(self):
        if self.class_teacher:
            for i, v in enumerate(self.class_teacher):
                print(i + 1, v.name)
        else:
            print("老师 %s 没有教任何班级")

    def show_teacher(self):
        if self.class_teacher:
            l = list()
            for i in self.class_teacher:
                l.append(i.name)
            s = " ".join(l)
            msg = '''
                - - - - - - - - - info of TEACHER - - - - - - - - -
                Name:    %s
                Age:     %s
                Class:   %s
                School:  %s
                - - - - - - - - - end - - - - - - - - -
                ''' % (self.name, self.age, s, self.school.name)
        else:
            msg = '''
                - - - - - - - - - info of TEACHER - - - - - - - - -
                Name:    %s
                Age:     %s
                School:  %s
                - - - - - - - - - end - - - - - - - - -
                ''' % (self.name, self.age, self.school.name)
        print(msg)



