# 【问题描述】
# 编写完成三个字符串排序的程序。
# 【输入形式】
# 输入三个字符串，每个一行，共三行。字符串不包括空格，每个字符串的长度不超过100个字节。
# 【输出形式】
# 按照字符串从大到小的顺序，一个字符串一行输出。
# 【样例输入】
# abc
# Adcs
# dsAd12
# 【样例输出】
# dsAd12
# abc
# Adcs

a = input()
b = input()
c = input()
list1 = [a,b,c]
list1.sort(reverse=True)
for i in list1:
    print(i)