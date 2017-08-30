# coding=utf-8
# TODO Python3 字符串
var1 = 'Hello World!'
var2 = "Runoob"
print "var1[0]: ", var1[0]
print "var2[1:5]: ", var2[1:5]
# 字符串拼接
print "已更新字符串: ", var1[:6] + 'Runoob!'
'''
Python转义字符:
\(在行尾时) —— 续行符
\\ —— 反斜杠符号
\' —— 单引号
\" —— 双引号
\a —— 响铃
\b —— 退格(Backspace)
\e —— 转义
\000 —— 空
\n —— 换行
\v —— 纵向制表符
\t —— 横向制表符
\r —— 回车
\f —— 换页
\oyy —— 八进制数，yy代表的字符，例如：\o12代表换行
\other —— 其它的字符以普通格式输出
'''
# \xyy —— 十六进制数，yy代表的字符，例如：\x0a代表换行
'''
Python字符串运算符:
下面实例变量a值为字符串 "Hello"，b变量值为 "Python"：
+ —— 字符串连接	a + b 输出结果： HelloPython
* —— 重复输出字符串	a*2 输出结果：HelloHello
[] —— 通过索引获取字符串中字符	a[1] 输出结果 e
[ : ] —— 截取字符串中的一部分	a[1:4] 输出结果 ell
in —— 成员运算符 - 如果字符串中包含给定的字符返回 True, H in a 输出结果 1
not in —— 成员运算符：如果字符串中不包含给定的字符返回 True, M not in a 输出结果 1
r/R —— 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。	print r'\n' prints \n 和 print R'\n' prints \n 
'''
a = "Hello"
b = "Python"
print"a + b 输出结果：", a + b
print"a * 2 输出结果：", a * 2
print"a[1] 输出结果：", a[1]
print"a[1:4] 输出结果：", a[1:4]
if "H" in a:
    print"H 在变量 a 中"
else:
    print"H 不在变量 a 中"
if "M" not in a:
    print"M 不在变量 a 中"
else:
    print"M 在变量 a 中"
print r'\n'
print R'\n'
'''
Python字符串格式化
'''
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
'''
%c	 格式化字符及其ASCII码
      %s	 格式化字符串
      %d	 格式化整数
      %u	 格式化无符号整型
      %o	 格式化无符号八进制数
      %x	 格式化无符号十六进制数
      %X	 格式化无符号十六进制数（大写）
      %f	 格式化浮点数字，可指定小数点后的精度
      %e	 用科学计数法格式化浮点数
      %E	 作用同%e，用科学计数法格式化浮点数
      %g	 %f和%e的简写
      %G	 %f 和 %E 的简写
      %p	 用十六进制数格式化变量的地址
'''
print 
'''Python三引号'''
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)
