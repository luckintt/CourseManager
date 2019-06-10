#__author__:Lenovo  "Yang Tian"
#date:2019/3/21

from conf import config
from dao import school

def exit_pro():
    print('Finish the operation in this level!')
    return True

def choose_sch():
    for index, sch_info in enumerate(config.SCHOOL):
        print(index + 1, sch_info["学校"].name)
    op = input('input school number>>>:').strip()
    if op.isdigit():
        op = int(op)
        if op > 0 and op <= len(config.SCHOOL):
            return  op - 1
        else:
            print("序号输入错误")
    else:
        print("序号输入错误")
    return -1

def create_sch():
    school_name = input("input school name>>>:").strip()
    for i in config.SCHOOL:
        if i["学校"].name == school_name:
            print("学校 %s 已存在" %school_name)
            return
    else:
        _school = school.School(school_name)
        config.SCHOOL.append({"学校":_school})

def create_tea():
    index = choose_sch()
    if index != -1:
        config.SCHOOL[index]["学校"].create_teacher()

def create_cls():
    index = choose_sch()
    if index != -1:
        config.SCHOOL[index]["学校"].create_class()

def create_cou():
    index = choose_sch()
    if index != -1:
        config.SCHOOL[index]["学校"].create_course()

def show_info():
    index = choose_sch()
    if index != -1:
        config.SCHOOL[index]["学校"].show_school()

def interactive():
    menu_top = u'''
                   - - - - - - - - Choose Option - - - - - - - -\033[32;1m
                   1.  创建学校
                   2.  创建讲师
                   3.  创建课程
                   4.  创建班级
                   5.  查看信息
                   6.  退出
                   \033[0m'''
    menu_top_dic = {
        '1': create_sch,
        '2': create_tea,
        '3': create_cou,
        '4': create_cls,
        '5': show_info,
        '6': exit_pro
    }
    exit_flag = False
    while not exit_flag:
        print(menu_top)
        choice = input('>>>:').strip()
        if choice in menu_top_dic:
            menu_top_dic[choice]()
            config.writeFile(config.INFO_FILE)
            if choice == '6':
                exit_flag = True
        else:
            print("\033[31;1mOption does not exist!\033[0m")

def login():  #检测登录是否成功
    count_unvaild = 0  # 输入的用户名无效次数
    while count_unvaild < 3:
        username = input("input login username>>>:").strip()
        if username == "admin":
            print("Welcome %s login...." % username)
            return True
        else:  # 若用户名不存在，则输出对应提示信息
            print("Username is not exist")
            count_unvaild += 1
    else:  # 当用户输入不存在的用户名达到三次时执行
        print('Username error for three times!')
        return False

def run():
    info = login()
    if info:  # 用户成功登录
        interactive()

if __name__ == '__main__':
    run()