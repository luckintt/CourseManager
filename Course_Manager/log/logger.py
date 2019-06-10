#__author__:Lenovo  "Yang Tian"
#date:2019/3/21

import time, json

time_format = '%Y-%m-%d %X'
time_current = time.strftime(time_format)

def logging(filename,content):
    with open(filename,'a',encoding='utf-8') as f:
        #json.dump('%s  %s  end action\n' % (time_current, content), f, ensure_ascii=False)
        f.write('%s  %s  end action\n' % (time_current, content))

if __name__ == '__main__':
    logging('学校操作日志','1111')

