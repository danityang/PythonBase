# coding=utf-8
print "Python基础篇2"
print "---------------------------------------------------------"
'''数据类型转换'''
x = "23"
int(x)
print x
print "---------------------------------------------------------"
"""逻辑运算符"""
a, b = 10, 20
print a and b
print a or b
print not a or b
# TODO 据自己的理解，a and b意为如果a,b值一样(都为True,或都为False)，返回a值，否则返回b值
# TODO a or b：如果a为True，它返回a的值，否则它返回b的值
# TODO not:结果的反值，相当于Java中的"!"
'''is和is not关键词'''
# TODO is，判断两个标识符是不是引用自一个对象， is not，判断两个标识符是不是引用自不同对象
a = 20
b = 20

if (a is b):
    print ("1 - a 和 b 有相同的标识")
else:
    print ("1 - a 和 b 没有相同的标识")

if (id(a) == id(b)):
    print ("2 - a 和 b 有相同的标识")
else:
    print ("2 - a 和 b 没有相同的标识")

# 修改变量 b 的值
b = 30
if (a is b):
    print ("3 - a 和 b 有相同的标识")
else:
    print ("3 - a 和 b 没有相同的标识")

if (a is not b):
    print ("4 - a 和 b 没有相同的标识")
else:
    print ("4 - a 和 b 有相同的标识")
# TODO is 与 == 区别：is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等