# coding=utf-8
# TODO Python列表
list1 = ['Google', 'Runoob', 1997, 2000];
list2 = [1, 2, 3, 4, 5];
list3 = ["a", "b", "c", "d"];
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
print
# TODO 更新列表
list = ['Google', 'Runoob', 1997, 2000]
print "第三个元素为 : ", list[2]
list[2] = 2001
print "更新后的第三个元素为 : ", list[2]
print
# TODO 删除列表元素
list = ['Google', 'Runoob', 1997, 2000]
print (list)
del list[2]
print "删除第三个元素 : ", list
print
# TODO 列表脚本操作符
# 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
'''
len([1, 2, 3])	 3	 长度
[1, 2, 3] + [4, 5, 6]	[1, 2, 3, 4, 5, 6]	 组合
['Hi!'] * 4	   ['Hi!', 'Hi!', 'Hi!', 'Hi!']	 重复
3 in [1, 2, 3]	 True	 元素是否存在于列表中
for x in [1, 2, 3]: print(x, end=" ")	 1 2 3	 迭代
'''
for list in [0, 1, 2]: print '列表迭代：', list
# TODO 列表截取与拼接
L = ['Google', 'Runoob', 'Taobao']
'''
L[2]	'Taobao'	读取第三个元素
L[-2]	'Runoob'	从右侧开始读取倒数第二个元素: count from the right
L[1:]	['Runoob', 'Taobao']	输出从第二个元素开始后的所有元素
'''
squares = [1, 4, 9, 16, 25]
print squares + [36, 49, 64, 81, 100]
print
# TODO 嵌套列表
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print x
print x[0]
print
