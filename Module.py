# coding=utf-8
import sys
# TODO 模块
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法

for i in sys.argv:
    print i
print sys.path
print
# TODO from…import 语句
# Python的from语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下
from Function import fun1
fun1
# TODO From…import* 语句
# 把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
from Function import *
# TODO __name__属性
# 一个模块被另一个程序第一次引入时，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
# 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入:
if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')

# TODO dir() 函数
# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
print dir(sys)
# 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称
print "dir(): ",dir()