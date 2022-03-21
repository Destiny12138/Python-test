# 【问题描述】试编写一个程序判断6位密码是否正确，若密码正确输出right，密码不正确输出wrong，如果输入的密码有非数字字符则输出wrong。密码规则是: 第i位数字是第i-1位数字加1后的3次方的个位数( 2<=i<=6)。
# 【输入形式】一个六位密码
# 【输出形式】"right" 或者"wrong"
# 【样例输入】272727
# 【样例输出】right
# 【样例说明】密码272727中第2位的7是第1位的2加1后的3次方的个位数。又，(7+1)的3次方为512，其个位数为2)，以此类推。

a = input()
try:
    b = int(a)
    # count = 0
    print('ringht' if all(int(a[i]) == ((int(a[i - 1]) + 1) ** 3) % 10 for i in range(1,6)) else 'wrong')
    # for i in range(1, 6):
    #     c = ((int(a[i - 1]) + 1) ** 3) % 10
    #     if int(a[i]) == c:
    #         count += 1
    # if count == 5:
    #     print("right")
    # else:
    #     print("wrong")
except:
    print("wrong")
