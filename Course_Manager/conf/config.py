#__author__:Lenovo  "Yang Tian"
#date:2019/3/21

import os, json, pickle
from dao import school, student, teacher, cls, course

SCHOOL_LOGFILE = r'../log/学校操作日志'
STUDENT_LOGFILE = r'../log/学员操作日志'
COURSE_LOGFILE = r'../log/课程操作日志'
TEACHER_LOGFILE = r'../log/讲师操作日志'
CLASS_LOGFILE = r'../log/班级操作日志'
INFO_FILE = r'../conf/all_info'


def obj_2_json():
    pass

def writeFile(filename):
    with open(filename, 'wb') as f_write:
        #json.dump(content, f_write, ensure_ascii=False)
        pickle.dump(SCHOOL, f_write)

def readFile(filename):
    size = os.path.getsize(filename)
    if size == 0:
        return  list()
    with open(filename, 'rb') as f_read:
        data = pickle.load(f_read)
        return data
        # try:
        #     return pickle.load(f_read)
        # except Exception as e:
        #     return list()

SCHOOL = readFile(INFO_FILE)# 利用列表SCHOOL来存储所有信息
print(SCHOOL)


