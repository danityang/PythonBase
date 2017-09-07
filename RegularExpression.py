# coding=utf-8
import re

# TODO 正则表达式
# re 模块使 Python 语言拥有全部的正则表达式功能。
# TODO re.match函数
# re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
'''
re.match(pattern, string, flags=0)
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
'''

'''
匹配对象方法
group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	    返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
'''
print "re.match: ", re.match('www', 'www.baidu.com').group()  # 在起始位置匹配
print "re.match: ", re.match('www', 'www.baidu.com').span()  # 不在起始位置匹配
line = "my name is danityang"
# matchObject = re.match(line, )
# TODO re.search方法
# re.search 扫描整个字符串并返回第一个成功的匹配。
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配
phone = "2004-959-559 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print "电话号码 : ", num

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print "电话号码 : ", num
