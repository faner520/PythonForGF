#!/usr/bin/env python3

s = ''
for i in range(1, 10):
    for j in range(1, i + 1):
        s += '{0}x{1}={2}\t'.format(j, i, j * i)
    s += '\n'
print(s)
