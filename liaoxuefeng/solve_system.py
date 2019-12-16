# -*- coding: utf-8 -*-

import math


# 解方程组

def quadratic(a, b, c):
    x = -b / (2 * a)
    y = math.sqrt(b ** 2 - 4 * a * c) / (2 * a)
    return x + y, x - y


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')
