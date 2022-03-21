# 【问题描述】
# 将n元（n是100的倍数）换成用10元、5
# 元、2
# 元的组合（其中每一面值都可取0）
# 【输入形式】
# 输入钱币总额n
# 【输出形式】
#
# 输出组合数
# 【样例输入】
#
# 100
# 【样例输出】
# 66

n = int(input())
a = int(n / 10)
b = int(n / 5)
c = int(n / 2)
sum = 0
for i in range(a + 1):
    for j in range(int((n - i * 10) / 5)+1):
        for k in range(int((n - i * 10 - j * 5) / 2)+1):
            if i * 10 + j * 5 + k * 2 == n:
                sum += 1
print(sum)
