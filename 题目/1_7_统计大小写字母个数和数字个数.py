# 【问题描述】统计一行字符的大写字母，小写字母和数字的个数。先输出大写字母个数，在输出小写字母个数，最后输出数字个数。
# 【输入形式】ljaij1A
# 【输出形式】1
#
#                         5
#
#                         1
# 【提示】用字符串的方法isupper, islower来判别大小写。isdigit来判断是否是数字。

a = input()
# list1 = list(a)
print(sum(i.isupper() for i in a))
print(sum(i.islower() for i in a))
print(sum(i.isdigit() for i in a))
# up = 0
# low = 0
# d = 0
# for x in list1:
#     b = str(x)
#     if b.isupper():
#         up +=1
#     elif b.islower():
#         low +=1
#     elif b.isdigit():
#         d +=1
# print(up)
# print(low)
# print(d)