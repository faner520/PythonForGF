# 最佳偷懒法

到现在为止，你是不是已经写过相当多的程序了？

我现在有个想法，写这样一个程序，首先计算等差数列的和，然后给出这个数列一共多少项？

```python
try:
    first = int(input("首项"))
    end = int(input("末项"))
    p = int(input("公差"))
    s = 0

    for i in range(first, end+1, p):
        s = s + i

    print("总和=", s)

    count = (end - first) / p + 1
    print("项数=", count)

except Exception:
    print("发生错误，退出")
```

好，我想你会这样写一个程序，但如果我让你不仅要求和、求项数，还要做其他的工作怎么办？

这个程序会变得很长，很复杂，然后你会觉得，改起来好麻烦！

现在我们换种做法：

## 函数（Function）

```python

# PEP-3107
def sum(first:int, end:int, p:int=1) -> int:
    s = 0
    for i in range(first, end+1, p):
        s = s + i
    return s

# Old Style
def count(first, end, p=1):
    return (end - first) / p + 1

try:
    f = int(input("首项"))
    e = int(input("末项"))
    p = int(input("公差"))

    s = sum(f, e, p)
    print("总和=", s)

    c = count(f, e, p)
    print("项数=", c)

except Exception:
    print("发生错误，退出")
```

这里出现了新的关键字`def`，用于定义一个函数。函数一般来讲有三部分：

1. 输入（也可能没有），这个被称为参数
2. 函数体，也就是具体执行哪些语句
3. 返回值（也可能没有）

当然，你也可以写一个空（Dummy）函数，但它不会起到任何作用

```python
# 没用的函数
def dummy_function():
    pass
```

现在我们先关注`count()`这个函数，在`def`这一行中，括号中的是参数列表，在调用这个函数的时候，参数应当是有一个确定的值的。

参数列表中`p=1`这个表示，这个参数是有默认值的，在调用时如果不指定，它就使用默认值。

然后在函数内部，有个关键字`return`，当程序执行到这一步的时候，将`return`后的值返回，停止执行下面的代码：

```python
def test():
    return "Hello"  # 返回一个字符串Hello
    print("Test")  # 这一句不会被执行
```

当然，`return`也可以什么都不返回，只是作为停止执行该函数的语句存在。

```python
def count(first, end, p=1):
    if p == 0:
        return  # 当p为0的时候，停止执行下面的语句，退出该函数
    return (end - first) / p - 1
```

现在再说一下一个函数体应该怎么写：

```python
def count(first, end, p=1):
    if p == 0:  # p 就是参数列表中的 p
        return  # 空返回
    return (end - first) / p - 1  # 返回后面表达式的执行结果
```

[TODO: Type hint]
