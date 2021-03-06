# coding=utf-8
import os, shutil, doctest, unittest
from datetime import date

# TODO Python 标准库
# 针对日常的文件和目录管理任务, mod:shutil 模块提供了一个易于使用的高级接口:
shutil.copyfile('H:\python_file_test.txt', 'H:\python_file_test2.txt')
# shutil.move('/build/executables', 'installdir')
now = date.today()
print now

# TODO 测试模块
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


# doctest.testmod()  # 自动验证嵌入测试


class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main()