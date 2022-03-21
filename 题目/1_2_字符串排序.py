# 【问题描述】输入字符串，按字典顺序从小到大排序，而后输出。
# 【输入形式】五个字符串，彼此之间用空格间隔。
# 【输出形式】将五个字符串排序输出
# 【样例输入】abcde C++ fghijkl Pascal Fortran
# 【样例输出】C++ Fortran Pascal abcde fghijkl

a = input()
b = a.split(' ')
b.sort()
c = ' '.join(b)
print(c)