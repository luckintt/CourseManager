#__author__:Lenovo  "Yang Tian"
#date:2019/3/21

from conf import config

class Student:
    def __init__(self, name, school, cls):
        self.name = name
        self.school = school
        self.cls = cls
        self.cur = list()  # [{课程，成绩}]
        for sch in config.SCHOOL:                             # 学生所在的学校
            if sch["学校"] == self.school:
                for index, _cls in enumerate(sch["班级"]):   # 学生所在的班级
                    if _cls.name == self.cls.name:
                        self.cur.append({"课程":sch["班级"][index + 1], "成绩": 0})
                break

    def show_grade(self):
        for i,v in enumerate(self.cur):
            print("%d  %s  %d" %(i + 1, v["课程"].name, v["成绩"]))

    def get_grade(self, course):
        for v in self.cur:
            if v["课程"].name == course.name:
                return v["成绩"]
        return -1

    def add_course(self, course):
        for v in self.cur:
            if v["课程"].name == course.name:
                print("该门课程已存在!")
                return
        self.cur.append({"课程": course, "成绩": 0})

    def change_cls(self, cls):
        self.cls.del_student(self)
        self.cls = cls
        self.cls.set_student(self)
        self.cur = list()
        for sch in config.SCHOOL:                             # 学生所在的学校
            if sch["学校"] == self.school:
                for index, _cls in enumerate(sch["班级"]):   # 学生所在的班级
                    if _cls.name == self.cls.name:
                        self.cur.append({"课程":sch["班级"][index + 1], "成绩": 0})
                break

    def show_student(self):
        l = list()
        for i in self.cur:
            l.append(i["课程"].name)
            l.append(str(i["成绩"]))
        s = " ".join(l)
        msg = '''
            - - - - - - - - - info of STUDENT - - - - - - - - -
            Name:    %s
            Course:  %s
            Class:   %s
            School:  %s
            - - - - - - - - - end - - - - - - - - -
            ''' % (self.name, s, self.cls.name, self.school.name)
        print(msg)


