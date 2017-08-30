# coding=utf-8
# TODO 列表推导式
vec = [2, 4, 6]
print [3 * x for x in vec]
print [[x, x * 2] for x in vec]
print  # 换行
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print [weapon.strip() for weapon in freshfruit]
print [3 * x for x in vec if x > 3]
print [3 * x for x in vec if x < 2]
print  # 换行
vec1 = [2, 4, 6]
vec2 = [4, 3, -9]
print [x * y for x in vec1 for y in vec2]
print [x + y for x in vec1 for y in vec2]
print [vec1[i] * vec2[i] for i in range(len(vec1))]
print  # 换行
# 列表推导式可以使用复杂表达式或嵌套函数：
print [str(round(355 / 113, i)) for i in range(1, 6)]
# TODO 嵌套列表解析
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]]
print "matrix[0] = ", matrix[0]
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print transposed
print  # 换行
# TODO del语句
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]  # 删除第一个元素
print a
del a[2:4]  # 删除第2-3位元素
print a
del a[:]  # 删除所有元素
print a
print  # 换行

# TODO 遍历技巧
# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print k, ":", v
print  # 换行

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到：
for i, v in enumerate(['tic', 'tac', 'toe']):
    print i, v

print  # 换行

# 同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

print  # 换行

# 要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数：
for i in reversed(range(1, 10, 2)):
    print(i)

print  # 换行

# 要按顺序遍历一个序列，使用sorted(),函数返回一个已排序的序列，并不修改原值：
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
