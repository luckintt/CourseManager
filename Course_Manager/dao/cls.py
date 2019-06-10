#__author__:Lenovo  "Yang Tian"
#date:2019/3/22

class Cls:
    def __init__(self, name, school):
        self.name = name
        self.school =school
        self.student_cls = list()

    def set_student(self, student):
        if student not in self.student_cls:
            self.student_cls.append(student)

    def del_student(self,student):
        if student  in self.student_cls:
            self.student_cls.remove(student)

    def show_student(self):
        if self.student_cls:
            for i, v in enumerate(self.student_cls):
                print(i + 1, v.name)
        else:
            print("班级 %s 没有任何学生" %self.name)

    def add_course(self, course):
        for i in self.student_cls:
            i.add_course(course)

    def show_cls(self):
        if self.student_cls:
            l = list()
            for i in self.student_cls:
                l.append(i.name)
            s = " ".join(l)
            msg = '''
               - - - - - - - - - info of CLASS - - - - - - - - -
               Name:    %s
               Student: %s
               School:  %s
               - - - - - - - - - end - - - - - - - - -
               ''' % (self.name, s, self.school.name)
        else:
            msg = '''
                - - - - - - - - - info of CLASS - - - - - - - - -
                Name:    %s
                School:  %s
                - - - - - - - - - end - - - - - - - - -
                ''' % (self.name, self.school.name)
        print(msg)