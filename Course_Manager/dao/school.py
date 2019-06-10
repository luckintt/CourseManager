#__author__:Lenovo  "Yang Tian"
#date:2019/3/21

from conf import config
from dao import course, teacher, student, cls
from log import logger

def exist_key(key_value):# 判断学校是否存在
    for i in config.SCHOOL:
        if i["学校"] == key_value:
            return True
    return False

def find_index(self):# 查询学校的下标
    for i in config.SCHOOL:
        if i["学校"] == self:  # 找到该学校
            return config.SCHOOL.index(i)
    return -1

class School:
    def __init__(self, name):
        self.name = name
        self.course_school = list()
        self.teacher_school = list()
        self.student_school = list()
        self.class_school = list()

    def create_course(self):
        course_name = input('input course name>>>:').strip()
        course_cycle = input('input course cycle>>>:').strip()
        course_cost = input('input course cost>>>:').strip()
        for cou_info in self.course_school:
            if course_name == cou_info.name:
                print('%s 中课程： %s 已存在' % (self.name, course_name))
                logger.logging(config.SCHOOL_LOGFILE, '%s 中课程： %s 已存在' % (self.name, course_name))
        else:
            _course = course.Course(course_name, course_cycle, course_cost, self)
            self.course_school.append(_course) # 课程是一个列表
            index = find_index(self)
            config.SCHOOL[index]["课程"] = self.course_school
            print('%s 创建课程： %s 成功' %(self.name, _course.name))
            logger.logging(config.SCHOOL_LOGFILE, '%s 创建课程： %s 成功' %(self.name, _course.name))

    def create_teacher(self):
        teacher_name = input('input teacher name>>>:').strip()
        teacher_age = input('input teacher age>>>:').strip()
        for tea_info in self.teacher_school:
            if teacher_name == tea_info.name:
                print('%s 中老师： %s 已存在' % (self.name, teacher_name))
                logger.logging(config.SCHOOL_LOGFILE, '%s 中老师： %s 已存在' % (self.name, teacher_name))
                break
        else:
            _teacher = teacher.Teacher(teacher_name, teacher_age, self)
            self.teacher_school.append(_teacher)
            index = find_index(self)
            config.SCHOOL[index]["老师"] = self.teacher_school
            print('%s 创建老师： %s 成功' % (self.name, _teacher.name))
            logger.logging(config.TEACHER_LOGFILE, '%s 创建老师： %s 成功' % (self.name, _teacher.name))
            logger.logging(config.SCHOOL_LOGFILE, '%s 创建老师： %s 成功' % (self.name, _teacher.name))

    def create_student(self):
        index = find_index(self)
        student_name = input('input regiest name>>>:').strip()
        if "学生" in config.SCHOOL[index]:
            for stu_info in config.SCHOOL[index]["学生"]:
                if student_name == stu_info.name:
                    print("Username %s exist...." % student_name)
                    return False
        for i,v in enumerate(self.class_school):
            print(i + 1, v.name)
        op = input('input class number>>>:').strip()
        if op.isdigit():
            op = int(op)
            if op > 0 and op <= len(self.class_school):
                _student = student.Student(student_name, self, self.class_school[op - 1])
                if _student not in self.student_school:
                    self.student_school.append(_student)
                    index = find_index(self)
                    config.SCHOOL[index]["学生"] = self.student_school
                    self.class_school[op - 1].set_student(_student)
                    logger.logging(config.STUDENT_LOGFILE, '%s 创建 %s 学生： %s 成功' % (self.name, self.class_school[op - 1].name, student_name))
                    logger.logging(config.CLASS_LOGFILE, '%s 添加学生： %s 成功' % (self.class_school[op - 1].name, student_name))
                    logger.logging(config.SCHOOL_LOGFILE, '%s 创建 %s 学生： %s 成功' % (self.name, self.class_school[op - 1].name, student_name))
                    print("Register Username %s successful...." % student_name)
                    return True
                else:
                    print("Register Username %s exist...." % student_name)
                    logger.logging(config.SCHOOL_LOGFILE, '%s 中学生： %s 已存在' % (self.name, student_name))
            else:
                print("序号输入错误")
        else:
            print("序号输入错误")
        return False

    def create_class(self):
        index = find_index(self)
        li = list()
        if "班级" in config.SCHOOL[index].keys():
            li = config.SCHOOL[index]["班级"]
        else:
            li = list()
        class_name = input('input class name>>>:').strip()
        for cls_info in self.class_school:
            if class_name == cls_info.name:
                _cls = cls_info
                break
        else:
            _cls = cls.Cls(class_name, self)
            self.class_school.append(_cls)
        print("请选择要上的课程：")
        for i,v in enumerate(self.course_school):
            print(i + 1, v.name)
        op = input('input course number>>>:').strip()
        if op.isdigit():
            op= int(op)
            if op > 0 and op <= len(self.course_school):
                print("请选择上课的老师：")
                for i, v in enumerate(self.teacher_school):
                    print(i + 1, v.name)
                op_t = input('input teacher number>>>:').strip()
                if op_t.isdigit():
                    op_t = int(op_t)
                    if op_t > 0 and op_t <= len(self.teacher_school):
                        li.append(_cls)
                        li.append(self.course_school[op - 1])
                        li.append(self.teacher_school[op_t - 1])
                        config.SCHOOL[index]["班级"] = li
                        _cls.add_course(self.course_school[op - 1])
                        self.course_school[op - 1].set_teacher(self.teacher_school[op_t - 1])
                        self.teacher_school[op_t - 1].set_class(_cls)
                        logger.logging(config.SCHOOL_LOGFILE, '%s 创建班级： %s 成功，课程为： %s，老师为： %s' % (self.name, _cls.name, self.course_school[op - 1].name, self.teacher_school[op_t - 1].name))
                        logger.logging(config.CLASS_LOGFILE, ' %s 班级在 %s 被创建' %( _cls.name, self.name))
                    else:
                        print("序号输入错误")
                else:
                    print("序号输入错误")
            else:
                print("序号输入错误")
        else:
            print("序号输入错误")

    def show_school(self):
        index = find_index(self)
        print("*****************************************\n学校 %s" %config.SCHOOL[index]["学校"].name)
        if "老师" in config.SCHOOL[index]:
            for tea_info in config.SCHOOL[index]["老师"]:
                tea_info.show_teacher()
        if "学生" in config.SCHOOL[index]:
            for stu_info in config.SCHOOL[index]["学生"]:
                stu_info.show_student()
        if "课程" in config.SCHOOL[index]:
            for stu_info in config.SCHOOL[index]["课程"]:
                stu_info.show_course()
        if "班级" in config.SCHOOL[index]:
            for stu_info in config.SCHOOL[index]["学校"].class_school:
                stu_info.show_cls()

if __name__ == "__main__":
    for i, v in enumerate(config.SCHOOL[0]["班级"]):
        if v.name == "1class" and config.SCHOOL[0]["班级"][i + 2].name == "张三":  # 是这个老师教的班级
            print(i + 1, config.SCHOOL[0]["班级"][i + 1].name)