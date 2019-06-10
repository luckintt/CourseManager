#__author__:Lenovo  "Yang Tian"
#date:2019/3/21

class Course:
    def __init__(self, name, cycle, cost, school):
        self.name = name
        self.cycle = cycle
        self.cost = cost
        self.__school = school
        self.__teacher = list()

    def set_teacher(self,teacher):
        if teacher not in self.__teacher:
            self.__teacher.append(teacher)

    def get_teacher(self):
        return self.__teacher

    def course_up(self, teacher):
        if teacher in self.__teacher:
            index = self.__teacher.index(teacher)
            self.__tearcher[index].salary += self.cost
        else:
            print("%s老师不教授课程%s" %(teacher.name, self.name))

    def show_course(self):
        if self.__teacher :
            l = list()
            for i in self.__teacher:
                l.append(i.name)
            s = " ".join(l)
            msg = '''
            - - - - - - - - - info of COURSE - - - - - - - - -
            Name:    %s
            Cycle:   %s
            Cost:    %s
            Teacher: %s
            School:  %s
            - - - - - - - - - end - - - - - - - - -
            ''' % (self.name, self.cycle, self.cost, s, self.__school.name)
        else:
            msg = '''
             - - - - - - - - - info of COURSE - - - - - - - - -
             Name:    %s
             Cycle:   %s
             Cost:    %s
             School:  %s
             - - - - - - - - - end - - - - - - - - -
             ''' % (self.name, self.cycle, self.cost, self.__school.name)
        print(msg)