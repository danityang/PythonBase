# coding=utf-8
import sys

# TODO Python错误和异常处理
# TODO try except语句块
i = 0
while i < 5:
    try:
        things = input("键盘输入")
        print things
        # 一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:
    except (NameError, ValueError, SyntaxError):
        print "not defined"
    i += 1

print
# 最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。
try:
    f = open('H:/python_file_test.txt', "r")
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
# except:
# print("Unexpected error:", sys.exc_info()[0])
# raise

print  # 换行
# try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。这个子句将在try子句没有发生任何异常的时候执行。例如:
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()

print  # 换行


def this_fails():
    x = 1 / 0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

# TODO 抛出异常
# Python 使用 raise 语句抛出一个指定的异常。例如：
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
