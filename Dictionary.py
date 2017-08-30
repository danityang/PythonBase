# coding=utf-8
# TODO Python字典
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号{}中 ,格式如下所示：
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# TODO 访问字典值
dict1 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print "dict['Name']: ", dict1['Name']
print "dict['Age']: ", dict1['Age']
# TODO 修改字典
dict1['Age'] = 8;  # 更新 Age
dict1['School'] = "Test Word"  # 添加信息
print dict1
# TODO 删除字典元素
del dict1['Name']  # 删除键 'Name'
dict1.clear()  # 删除字典
del dict1  # 删除字典
# TODO 字典键的特性
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
print "dict['Name']: ", dict['Name']
# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：
dict = {['Name']: 'Runoob', 'Age': 7}
print "dict['Name']: ", dict['Name']
