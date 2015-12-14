#!/usr/bin/env python3

import math

a = float(input('输入一个数字：'))
if a > 0:
    print(math.log(a))  # 也可以用 math.log10(a) / math.log10(math.e)
else:
    print('输入错误')
