# coding=utf-8
print "Python基础篇1"
print "---------------------------------------------------------"
'''list列表用法、写法'''
list = ['abcd', 700, 2.35, "dehi", 70.23]
print list[0]
print list[3:]
print list[2:5]
print list * 2
# 列表中的元素是可以改变的：
list[0] = "efgd"
print list[0]
# todo 注：list[2:5]表示截取2——>5的元素，但不包括5：如下
list[2:6] = "hhhh", "5678", 3333, 5j
print list[2:6]
print "---------------------------------------------------------"
'''Tuple(元组)'''
# todo Tuple(元组)：与list不同的是，它的元素不能修改
# tuple元组写在小括号“()”里，元素之间用逗号隔开：
tupleExp = ("abce", 66666, 34j, 78.01, '45')
tupleExp2 = ("Test", 899, 55j, 78.9, 45)
print tupleExp[0]
print tupleExp[2:5]
print tupleExp * 2
print tupleExp + tupleExp2  # 拼接
'''Set(集合)'''
# todo Set(集合):无序不重复元素的序列，相当于Java中的Map集合'''
setVar = {"name", "sex", "age", "address"}
print setVar  # 输出集合，重复的元素被自动去掉
if "name" in setVar:
    print "name在setVar中"
else:
    print "name不在setVar中"
# TODO in 关键词，表示在序列中，返回True,否则返回false,还有not in，表示没有在序列中找到词返回True,否则返回False
print "---------------------------------------------------------"
# todo 集合运算
a = set("gdhhjk")
b = set("hhsuhuij")
print "a: ", a
print "b: ", b
print a - b  # a和b的差集
print a | b  # a和b的差集
print a & b  # a和b的交集
print a ^ b  # a和b中不同时存在的元素
print "---------------------------------------------------------"
'''Dictionary（字典）'''
# todo 字典是一种映射类型，字典用"{ }"标识，它是一个无序的键(key) : 值(value)对集合
dict = {}
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
dict['one'] = "这是value"  # 键值对
dict[2] = "这也是value"  # 键值对
print dict['one']
print dict[2]
print dict.keys()  # 输出所有键
print dict.values()  # 输出所有值
