#__author__:Lenovo  "Yang Tian"
#date:2018/8/9

import sys, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 找到根路径  ATM
sys.path.append(BASE_DIR)

from core import  main
main.run()