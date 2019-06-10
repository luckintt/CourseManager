#__author__:Lenovo  "Yang Tian"
#date:2018/8/9

from conf import config
from log import logger

def exit_pro(info):
    print('Finish the operation in this level!')
    return True

def search_grade(info):
    info[1].show_grade()

def change_class(info):
    index = config.SCHOOL.index(info[2])
    for i, cls_info in enumerate(config.SCHOOL[index]["学校"].class_school):
        print(i + 1, cls_info.name)
    op = input('input class number>>>:').strip()
    if op.isdigit():
        op = int(op)
        if op > 0 and op <= len(config.SCHOOL[index]["学校"].class_school):
            old_cls = info[1].cls.name
            info[1].change_cls(config.SCHOOL[index]["学校"].class_school[op - 1])
            logger.logging(config.STUDENT_LOGFILE, '%s 学生更换班级 %s 为 %s 成功' % (info[1].name, old_cls, info[1].cls.name))
        else:
            print("序号输入错误")
    else:
        print("序号输入错误")

def register():
    for index, sch_info in enumerate(config.SCHOOL):
        print(index + 1, sch_info["学校"].name)
    op = input('input school number>>>:').strip()
    if op.isdigit():
        op = int(op)
        if op > 0 and op <= len(config.SCHOOL):
            return config.SCHOOL[op - 1]["学校"].create_student()
        else:
            print("序号输入错误")
    else:
        print("序号输入错误")
    return False

def login():  #检测登录是否成功
    count_unvaild = 0  # 输入的用户名无效次数
    while count_unvaild < 3:
        username = input("input login username>>>:").strip()
        for sch_info in config.SCHOOL:
            if "学生" in sch_info:
                for stu_info in sch_info["学生"]:
                    if username == stu_info.name:
                        print("Welcome %s login...." % username)
                        return True, stu_info, sch_info
        else:  # 若用户名不存在，则输出对应提示信息
            print("Username is not exist")
            count_unvaild += 1
    else:  # 当用户输入不存在的用户名达到三次时执行
        print('Username error for three times!')
        return False, None

def interactive(info):
    menu_top = u'''
             - - - - - - - - Choose Option - - - - - - - -\033[32;1m
            1.  查看成绩
            2.  换班
            3.  退出
            \033[0m'''
    menu_top_dic = {
        '1': search_grade,
        '2': change_class,
        '3': exit_pro
    }
    while True:
        print(menu_top)
        choice = input('>>>:').strip()
        menu_top_dic[choice](info)
        config.writeFile(config.INFO_FILE)
        if choice == '3':
            return

def run():
    menu_top = u'''
                   - - - - - - - - Choose Option - - - - - - - -\033[32;1m
                   1.  学员注册
                   2.  学员登录
                   3.  退出
                   \033[0m'''
    menu_top_dic = {
        '1': register,
        '2': login,
        '3': exit_pro
    }
    exit_flag = False
    while not exit_flag:
        print(menu_top)
        choice = input('>>>:').strip()
        if choice in menu_top_dic:
            if choice == '3':
                print("exit successful")
                return
            if choice == '1' and menu_top_dic[choice]() == False:
                continue
            config.writeFile(config.INFO_FILE)
            info = menu_top_dic['2']()
            if True in info:  # 用户成功登录
                interactive(info)
        else:
            print("\033[31;1mOption does not exist!\033[0m")

if __name__ == '__main__':
    run()