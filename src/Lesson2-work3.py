#!/usr/bin/env python3

a = int(input('a='))
b = int(input('b='))

# 此处给出一个解法
r = 0
for i in range(10):
    if (b & (1 << i)) >> i == 1:
        r += (a << i)

print('{0} x {1} = {2}'.format(a, b, r))
