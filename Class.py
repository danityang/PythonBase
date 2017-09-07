# coding=utf-8
class MyFirstClass:
    i = 65536

    # TODO __init__方法是类的构造方法
    def __init__(self, a, b):
        self.c = a
        self.d = b
        print "my first class"


cla = MyFirstClass("ertg", 56)
print cla.i
print cla.c, cla.d


# TODO 类方法
# 类的方法必须有一个额外的第一个参数名称, 按照惯例它的名称是 self

class Test:
    def __init__(self):
        print "类的默认（构造）方法"

    def claMeth0d(self):
        print self
        print "类方法"


classTest = Test()
print classTest.claMeth0d()


# TODO self代表的是类的实例
# self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的
class People:
    "定义累的属性"
    name = "张三"
    age = 22
    "定义累的私有属性，外部无法直接访问"
    __weight = 95

    # 构造方法
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def speak(self):
        print "{0}说: {1}".format(self.name, "扫描？")


classPeople = People("太阳镜", 22, 95)
print classPeople.speak()

# TODO Python继承
# Python支持类的继承，如果一种语言不支持继承，类就没有什么意义。派生类的定义如下所示:
'''
class DerivedClassName(BaseClassName1):
    <statement-1>
    .
    .
    .
    <statement-N>
'''

# 需要注意圆括号中基类的顺序，若是基类中有相同的方法名，而在子类使用时未指定，python从左至右搜索
# 即方法在子类中未找到时，从左到右查找基类中是否包含方法。
# BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:

'''
class DerivedClassName(modname.BaseClassName):
'''


class XiaoLi(People):
    grade = '三年级'

    def __init__(self, name, age, weight, grade):
        People.__init__(self, name, age, weight)
        self.grade = grade

    def speak(self):
        print "{0}说：我就是{1}，年龄{2}, 现在在上{3}年级".format(self.name, self.name, self.age, self.grade)


classX = XiaoLi("小米", 25, 150, 6)
print classX.speak()

# TODO Python多继承
# Python同样有限的支持多继承形式。多继承的类定义形如下例:
'''
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

'''


class Sample(People, XiaoLi):
    theme = ''

    def __init__(self, name, age, weight, grade, theme):
        People.__init__(self, name, age, weight)
        XiaoLi.__init__(self, name, age, weight, grade)
        self.theme = theme

    def speak(self):
        print "{0}说：我叫{1}，年龄{2}，现在在读{3}年级，我今天演讲的主题是《{4}》，" \
            .format(self.name, self.name, self.age, self.grade, self.theme)


classDjc = Sample("金粉细雨", 19, 93, 12, "有效的学习方法")
print classDjc.speak()


# TODO 方法重写
class Parent:  # 定义父类
    def myMethod(self):
        print ('调用父类方法')


class Child(Parent):  # 定义子类
    def myMethod(self):
        print ('调用子类方法')


c = Child()  # 子类实例
c.myMethod()  # 子类调用重写方法


# TODO 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类地外部调用。self.__private_methods。

class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def __init__(self):
        print ""

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)


counter = JustCounter()
counter.count()
print (counter.publicCount)
print (counter.__secretCount)  # 报错，实例不能访问私有变量


class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()


x = Site('菜鸟教程', 'www.runoob.com')
x.who()  # 正常输出
x.foo()  # 正常输出
x.__foo()  # 报错

# TODO 类的专有方法：
'''
    __init__ : 构造函数，在生成对象时调用
    __del__ : 析构函数，释放对象时使用
    __repr__ : 打印，转换
    __setitem__ : 按照索引赋值
    __getitem__: 按照索引获取值
    __len__: 获得长度
    __cmp__: 比较运算
    __call__: 函数调用
    __add__: 加运算
    __sub__: 减运算
    __mul__: 乘运算
    __div__: 除运算
    __mod__: 求余运算
    __pow__: 乘方
'''


# TODO 运算符重载
# Python同样支持运算符重载，可以对类的专有方法进行重载，实例如下：
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print (v1 + v2)
