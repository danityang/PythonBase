# coding=utf-8
# TODO for循环语句
# Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。
# for循环的一般格式如下：
languages = ["C", "C++", "Perl", "Python"]
for var in languages:
    print (var)

# TODO break语句
sites = ["Baidu", "Google", "Runoob", "Taobao"]
# for 后面的跟着的是自定义的变量，意为把循环迭代的值赋值给它
for f in sites:
    if f == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + f)
else:
    print("没有循环数据!")
print("完成循环!")
print
# TODO range()函数
# 如果需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如:
for i in range(5):
    print(i)
print
# 也可以使用range指定区间的值：
for i in range(5, 9):
    print(i)
print
# 可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for i in range(0, 10, 3):
    print(i)
print
for i in range(-10, -100, -30):
    print(i)
print
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print i, a[i]
print
# TODO break和continue语句及循环中的else子句
# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。 实例如下:
for letter in 'Runoob':  # 第一个实例
    if letter == 'b':
        break
    print '当前字母为 :', letter

var = 10
while var > 0:
    print '当期变量值为 :', var
    var = var - 1
    if var == 5:
        break
print ("Good bye!")
print
# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print n, '等于', x, '*', n // x
            break
    else:
        # 循环中没有找到元素
        print n, ' 是质数'
print
# TODO pass 语句
# pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句，如下实例
'''while True:
    pass  # 等待键盘中断 (Ctrl+C)
'''
# 以下实例在字母为 o 时 执行 pass 语句
for le in 'Runoob':
    if le == 'o':
        pass
        print '执行 pass 块'
        print '当前字母 :', le
print ("Good bye!")
