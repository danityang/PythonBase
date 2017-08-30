# coding=utf-8
print ("Python基础0篇")
# 注释写法1
'''注释写法2'''
print ("注释写成'#'或者'''")
word = "字符串"
sentence = "这是一句话"
print word
print sentence
# input("\n\n按 enter 退出")
print "\n"  # 换行
intVar = 1000
floatVar = 1000.0
nameString = "我的名字"
print intVar
print (floatVar)
print (nameString)
'''变量的赋值'''
a, b, c, d = 20, 5.5, True, 4 + 3j
# 查看数据类型，使用type()，或isinstance()函数
print type(a), type(b), type(c), type(d)
print isinstance(a, int)
str = 'Runoob'
print (str)  # 输出字符串
print (str[0:-1])  # 输出第一个到倒数第二个的所有字符
print (str[0])  # 输出字符串第一个字符
print (str[2:5])  # 输出从第三个开始到第五个的字符
print (str[2:])  # 输出从第三个开始的后的所有字符
print (str * 2)  # 输出字符串两次
print (str + "TEST")  # 连接字符串
print "--------------------------------------------------------"
# Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
print 'Ru\noob'
print r'Ru\noob'
word = "danityang"
# Python中的字符串有两种索引方式，从左往右以0开始，从右往左以-1开始
print (word[0], word[8])
print (word[-1], word[-4], word[-9])

