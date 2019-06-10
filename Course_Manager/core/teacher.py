#__author__:Lenovo  "Yang Tian"
#date:2018/8/9

from conf import config
from log import logger

def exit_pro(info):
    print('Finish the operation in this level!')
    return True

def see_class(info):
    info[1].show_class()
    pass

def see_student(info):
    see_class(info)
    op = input('input class number>>>:').strip()
    if op.isdigit():
        op = int(op)
        if op > 0 and op <= len(info[1].class_teacher):
            info[1].class_teacher[op - 1].show_student()
        else:
            print("序号输入错误")
    else:
        print("序号输入错误")

def edit_student_grade(info):
    stu_name = input('input student name>>>:').strip()
    for cls_v in info[1].class_teacher:
        for stu_v in cls_v.student_cls:
            if stu_name == stu_v.name:                     # 找到该学生所在的班级
                l = list()
                count = 1
                for i, v in enumerate(info[2]["班级"]):
                    if v.name == cls_v.name and info[2]["班级"][i + 2].name == info[1].name: #是这个老师教的班级
                        grade = stu_v.get_grade(info[2]["班级"][i + 1])
                        print(count, info[2]["班级"][i + 1].name, grade)
                        l.append(i + 1)                    # 将课程下标加入列表
                        count += 1
                op = input('input course number>>>:').strip()
                if op.isdigit():
                    op = int(op)
                    if op > 0 and op < count:
                        new_grade = int(input('input new grade>>>:').strip())
                        if info[1].edit_grade(stu_v, info[2]["班级"][l[op - 1]], new_grade):
                            logger.logging(config.TEACHER_LOGFILE, '%s 更改 %s 学生 %s 课程的成绩 %d  为 %d成功' % (info[1].name, stu_name, info[2]["班级"][l[op - 1]].name, grade, new_grade))
                            print("成绩修改成功")
                        else:
                            print("该学生没有此课程")
                    else:
                        print("序号输入错误")
                else:
                    print("序号输入错误")
                return
    else:
        print("该老师没有教授此学生")

def login():  #检测登录是否成功
    count_unvaild = 0  # 输入的用户名无效次数
    while count_unvaild < 3:
        username = input("input login username>>>:").strip()
        for sch_info in config.SCHOOL:
            if "老师" in sch_info:
                for tea_info in sch_info["老师"]:
                    if username == tea_info.name:
                        print("Welcome %s login...." % username)
                        return True, tea_info, sch_info
        else:  # 若用户名不存在，则输出对应提示信息
            print("Username is not exist")
            count_unvaild += 1
    else:  # 当用户输入不存在的用户名达到三次时执行
        print('Username error for three times!')
        return False, None

def interactive(info):
    menu_top = u'''
             - - - - - - - - Choose Option - - - - - - - -\033[32;1m
             1.  查看班级
             2.  查看班级学员列表
             3.  修改学员成绩
             4.  退出
             \033[0m'''
    menu_top_dic = {
        '1': see_class,
        '2': see_student,
        '3': edit_student_grade,
        '4': exit_pro
    }
    exit_flag = False
    while not exit_flag:
        print(menu_top)
        choice = input('>>>:').strip()
        if choice in menu_top_dic:
            menu_top_dic[choice](info)
            config.writeFile(config.INFO_FILE)
            if choice == '4':
                exit_flag = True
        else:
            print("\033[31;1mOption does not exist!\033[0m")

def run():
    info = login()
    if True in info:  # 用户成功登录
        interactive(info)

if __name__ == '__main__':
    run()