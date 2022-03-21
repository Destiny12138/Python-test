# 【问题描述】
# 编写与字符串对象的find方法功能相似的函数find(srcString, substring, start,
#                            end)，作用是在srcString串的下标start到下标end之间的片段中寻找subString串的所有出现。如果有多处出现，各下标位置用西文逗号
# ','
# 隔开。如果一次都没有出现，则输出
# "none"。
# 【输入形式】
# 按照somestrig, substring, start, end的顺序输入，之间由空格隔开。somestring和substring均由A / T / C / G四个字母组成。start和end由自然数构成。
# 【输出形式】当匹配成功时，输出子串在DNA字符串的所有位置，以子串第一个字母在DNA字符串中匹配位置的下标（从0开始），中间用西文逗号
# ","
# 隔开；当匹配失败时，输出
# "none"。
# 【样例输入】ATGGCTGATGGC
# TGG
# 0
# 11
# 【样例输出】1, 8
# 【样例输入】ATGGCTGATGGC
# TTT
# 0
# 11
# 【样例输出】none

def find(someString, substring,start,end):
    result = []
    a = -1
    while substring in someString[start:end]:
        b = someString[start:end]
        a = someString[start:end].find((substring))+a+1
        result.append(str(a))
        start = a+1
    if len(result) != 0:
        print(",".join(result))
    else:
        print("none")

if __name__ == "__main__":
    somestrig, substring, start, end = tuple(input().split(" "))
    start = int(start)
    end = int(end)
    find(somestrig, substring,start,end)