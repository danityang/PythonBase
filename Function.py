# coding=utf-8
# TODO Python函数
# 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
# 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
# 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
# 函数内容以冒号起始，并且缩进。
# return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
def hello():
    print("Hello Python!")


print
# 函数调用
hello()

print


# 计算面积函数
def area(width, height):
    return width * height


def print_welcome(name):
    print "Welcome", name


# 函数调用
print_welcome("Python")

w = 4
h = 5
print "width =", w, " height =", h, " area =", area(w, h)


# TODO 函数传递可变/不可变对象
# 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
# TODO 函数传递不可变对象，只是修改另一个复制的对象，不会影响本身，如下：
def changeInt(a):
    "传递不可变对象"
    a = 10


b = 20
changeInt(b)
# b的值仍旧是20
print b
print


# TODO 函数传递可变对象，则是将对象真正的传过去，修改后外部对象也会受影响，如下：
def changeName(mlist):
    "传递可变对象"
    mlist.append([34, 56, 78, "dfd"])
    print "方法内部：", mlist


list = ["testword", 99, 0.545]
changeName(list)
print "方法外部：", list;
print


# TODO 函数不定长参数
# 加了星号（*）的变量名会存放所有未命名的变量参数。如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出1: ", arg1
    for var in vartuple:
        print "输出2: ", var


printinfo(10)
printinfo(10, 'dfg', 89, 3j)
print
# TODO 匿名函数
# python 使用 lambda 来创建匿名函数。

# lambda 只是一个表达式，函数体比def 简单很多。
# lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
# lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
# 虽然lambda函数看起来只能写一行，却不等同于C或C + +的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2

# 调用sum函数
print "相加后的值为 : ", sum(10, 20)
print "相加后的值为 : ", sum(20, 20)
print


# TODO return语句
# return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print "函数内 : ", total
    return total


# 调用sum函数
total = sum(10, 20)
print "函数外 : ", total
print
# TODO 变量作用域
# Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
# 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4中，分别是：
'''
    L （Local） 局部作用域
    E （Enclosing） 闭包函数外的函数中
    G （Global） 全局作用域
    B （Built-in） 内建作用域
'''
# TODO 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
# TODO 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中
total = 0;  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print "函数内是局部变量 : ", total
    return total;


# 调用sum函数
sum(10, 20);
print "函数外是全局变量 : ", total
print
# TODO global 和 nonlocal关键字
# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
num = 1


def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)


fun1()


# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了
def outer():
    num = 10
    def inner():
        # nonlocal num  # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)


outer()
