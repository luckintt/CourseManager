#__author__:Lenovo  "Yang Tian"
#date:2018/8/9

from conf import config
from core import  student,teacher,admin

def exit_pro():
    config.writeFile(config.INFO_FILE, config.SCHOOL)
    print('Finish the operation in this level!')
    return True

def interactive_top():
    menu_top = u'''
               - - - - - - - - Choose Option - - - - - - - -\033[32;1m
               1.  学员视图
               2.  讲师视图
               3.  管理员视图
               4.  退出
               \033[0m'''
    menu_top_dic = {
        '1': student.run,
        '2': teacher.run,
        '3': admin.run,
        '4': exit_pro
    }
    exit_flag = False
    while not exit_flag:
        print(menu_top)
        choice = input('>>:').strip()
        if choice in menu_top_dic:
            menu_top_dic[choice]()
            if choice == '4':
                exit_flag = True
        else:
            print("\033[31;1mOption does not exist!\033[0m")

def run():
    interactive_top()













