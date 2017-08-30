# coding=utf-8
# TODO 斐波纳契数列:
a, b = 0, 1
while b < 100:
    print a
    a, b = b, a + b
# TODO 条件控制语句
var1 = 100
if var1:
    print ("1 - if 表达式条件为 true")
    print (var1)

# TODO Python中，布尔值0为False，1为True;
var2 = 0
if var2:
    print ("2 - if 表达式条件为 true")
    print (var2)
print ("Good bye!")
print
age = int(input("请输入你家狗狗的年龄: "))
print("")
if age < 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2) * 5
    print"对应人类年龄: ", human
print
number = 7
guess = -1
print("数字猜谜游戏!")
while guess != number:
    guess = int(input("请输入你猜的数字："))

    if guess == number:
        print("恭喜，你猜对了！")
    elif guess < number:
        print("猜的数字小了...")
    elif guess > number:
        print("猜的数字大了...")

# TODO if 嵌套
'''
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
'''
# TODO while 循环
n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))
# TODO 无限循环
var = 1
while var == 1:  # 表达式永远为 true
    num = int(input("输入一个数字  :"))
    print "你输入的数字是: ", num

print ("Good bye!")
# TODO while 循环使用 else 语句
# 在 while … else 在条件语句为 false 时执行 else 的语句块
count = 0
while count < 5:
    print (count, " 小于 5")
    count = count + 1
else:
    print (count, " 大于或等于 5")


