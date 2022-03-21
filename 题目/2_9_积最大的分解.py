# 【问题描述】从键盘输入一个正整数n(n>1)，该正整数可以分解成两个正整数k1和k2之和（允许k1和k2相等）。请编写一个函数求使两个正整数的乘积最大的分解方案，并返回乘积max。
# 【输入形式】标准输入的一行表示正整数n
# 【输出形式】标准输出的一行表示最大乘积max，若输入的数据不合法（如：负整数、0或1），输出"illegal input"。
# 【样例输入】20
# 【样例输出】100
# 【样例说明】20=10 + 10，此时积最大，为100。

a = int(input())
maxNum = 0
if a < 2:
    print("illegal input")
else:
    for i in range(1, a // 2 + 1):
        b = i * (a - i)
        if b > maxNum:
            maxNum = b
    print(maxNum)
