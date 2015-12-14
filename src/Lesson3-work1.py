#!/usr/bin/env python3

a = int(input('现在你的年龄是:'))
if a >= 18:
    print('啊！已经成年了')
elif a < 18 and a >=12:
    print('青春期')
elif a >= 0 and a < 12:
    print('小P孩')
else:
    print('输入错误')
