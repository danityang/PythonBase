# coding=utf-8
import math

# TODO Python3输入输出
# 使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
# 使用 str.format() 函数来格式化输出值。
# 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
# TODO str()： 函数返回一个用户易读的表达形式。
# TODO repr()： 产生一个解释器易读的表达形式。
s = "hello,python3"
print str(s)
print repr(s)
print str(1 / 7)
print repr(10 * 3.25)
print repr(200 * 200)
#  repr() 函数可以转义字符串中的特殊字符
hello = 'hello, runoob\n'
hellos = repr(hello)
print hellos
print  # 换行
# repr() 的参数可以是 Python 的任何对象
'''
repr((x, y, ('Google', 'Runoob')))
'''
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

print  # 换行
# TODO str.format() 的基本使用:
print('{}网址： "{}!"'.format('百度', 'www.baidu.com'))
# 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
# 在括号中的数字用于指向传入对象在 format() 中的位置，如下所示
print('{0} 和 {1}'.format('Google', 'Runoob'))
print('{1} 和 {0}'.format('Google', 'Runoob'))
# 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
print "{int},{word}".format(int=34, word='test word')
# 位置及关键字参数可以任意的结合:
print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
print  # 换行
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
# 保留小数点后3位
print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
print  # 换行
# 在 “:” 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name, number in table.items():
    print('{0:10} ——> {1:10}'.format(name, number))
print  # 换行
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]}; Google: {0[Google]}; Taobao: {0[Taobao]}'.format(table))
print('Runoob: {Runoob}, Google: {Google}, Taobao: {Taobao}'.format(**table))
print  # 换行
# TODO 旧式字符串格式化
# "%"操作符也可以实现字符串格式化。 它将左边的参数作为类似 sprintf() 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串. 例如:
print('常量 PI 的值近似为：%5.3f。' % math.pi)
print('值为：%0.3f' % 5)
print  # 换行
# TODO 读取键盘输入
input_str = input("请输入：")
print "你输入的内容是: ", input_str
print  # 换行
# TODO 读和写文件
# open()函数将会返回一个 file 对象，基本语法格式如下:
'''
open(filename, mode)
'''
# filename：一个包含了你要访问的文件名称的字符串值。
# mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
# r	    以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
# rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# w	    打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a	    打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

# 在本地电脑磁盘H上创建/打开一个文件
file_path = "H:/python_file_test.txt"
f = open(file_path, "w")
f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n")
# 关闭打开的文件
f.close()
print "Create File Success"
print  # 换行

# TODO 文件对象的方法
'''
f.read()
读取一个文件的内容，调用 f.read(size),
'''
# size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
f = open(file_path, "r")
print "文件内容: ", f.read()
f.close()
print  # 换行

'''
f.readline()
f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
'''
f = open(file_path, "r")
print "f.readline(): ", f.readline()
f.close()
print

'''
f.readlines()
f.readlines() 将返回该文件中包含的所有行。如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。 
'''
f = open(file_path, "r")
print "f.readlines(): ", f.readlines()
f.close()
# 使用迭代法读取文件
f = open(file_path, "r")
for line in f:
    print "迭代读取文件： ", line
f.close()
'''
f.write()
将string 写入到文件中, 然后返回写入的字符数。
'''
f = open(file_path, "a")
f.write("再来写几句话到里面测试测试\n")
print "写入成功"
print  # 换行
f.close()
# 如果要写入一些不是字符串的东西, 那么将需要先进行转换:
f = open(file_path, "a")
value = 345
s = str(value)
f.write(s)
f.close()
print "写入成功"
'''
f.tell()
返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。 
'''
f = open(file_path, "a")
print "f.tell(): ", f.tell()
f.close()
'''
f.seek()
如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数
 from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
    seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
    seek(x,1) ： 表示从当前位置往后移动x个字符
    seek(-x,2)：表示从文件的结尾往前移动x个字符 
from_what 值为默认为0，即文件开头。
'''
f = open(file_path, "rb+")
f.write('0123456789abcdef')
f.seek(5)  # 移动到文件的第六个字节
print f.read(1)
f.seek(-3, 2)  # 移动到文件的倒数第三字节
print f.read(1)
'''
f.close()
在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。
当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。
'''

# TODO pickle 模块
