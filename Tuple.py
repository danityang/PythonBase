# coding=utf-8
# TODO Python元组
# 元组与列表类似，不同之处在于元组的元素不能修改。元组使用小括号，列表使用方括号。元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
# 创建空元组
tup = ()
# 当元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
tup4 = (50)
print type(tup4)
tup5 = (50,)
print type(tup5)
# TODO 访问元组
print tup1[0]
print tup2[2]
# TODO 修改元组
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print tup3
print
# TODO 删除元组
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:
tup = ('Google', 'Runoob', 1997, 2000)
print (tup)
del tup;
print ("删除后的元组 tup : ")
print tup
# TODO 元组运算符
'''
len((1, 2, 3))	3	计算元素个数
(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
('Hi!',) * 4 	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
3 in (1, 2, 3)	True	元素是否存在
for x in (1, 2, 3): print x,	1 2 3	迭代 
'''
