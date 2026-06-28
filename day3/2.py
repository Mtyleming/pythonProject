# 字符串处理
#
# 需求：实现文本统计功能
# 思路：1) 输入一段文本 2) 统计字符数、单词数、行数 3) 查找替换功能

s = input("请输入一段文本")

print(s.__len__())
print(s.split().__len__())
print(s.split("\n").__len__())

print(s)
print(s.replace(input("请输入准备替换的文字"),input("请输入替换后文字")))

print(len(s))

