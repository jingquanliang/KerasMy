#encoding=utf-8
__author__ = 'jql'

import os,sys

#解决import跨目录引用问题（两种方法）
#第一种方法：也可以在sublime-build 文件中添加以下的说明实现
#该方法适用于用ctrl+B运行的方式
# "env":
#     {
#         "PYTHONPATH": "path/to/a/folder:path/to/another/folder", #linux 用冒号
#		  "PYTHONPATH": "D:/PythonWorkSpace/KerasMy;D:/PythonWorkSpace/scienceTest" #windows 可以用分号
#     }

#完成的如下所示#####  新建new-build-sytem，然后输入以下的东西，保存即可
# {
# 	"cmd": ["D:/software/Anaconda2/python.exe", "-u", "$file"],
# 	"file_regex": "^[ ]*File \"(...*?)\", line([0-9]*)",
# 	"selector": "source.python",
# 	"env":
#     {
#          "PYTHONPATH": "D:/PythonWorkSpace/KerasMy;D:/PythonWorkSpace/scienceTest"
#     }
# }
#######################

#第二种方法，加入路径
# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(parentdir)
# sys.path.insert(0,parentdir)

print(os.sys.path)
from test import justTest

# def justTest1():
#     print("jsldjflsjdfsljflsdjfljsdlf")

if __name__ == "__main__":
    print("main")
    # print "sdljf"
    # print(sys.path)
    # main()
    justTest()
