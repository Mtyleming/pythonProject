########三角形面积函数
def triangle_area(b,h):
    return (b*h)/2

print(f"三角形:3为底4为高的面积是{triangle_area(3,4)}")

########一段英文字符串 统计元音字母的数量(aeiouAEIOU)
def count(count_str):
    """

    :param count_str:英文字符串
    :return: 元音字母的数量
    """
    resList = [ i for i in count_str if i in "aeiouAEIOU"]
    print(f"输入的字符串中元音字母有{len(resList)}个")

# count(input("请输入一段英文字符串"))

###########
def huiwen(huiwen_str):
    if huiwen_str == huiwen_str[::-1]:
        return "是"
    else:
        return "不是"
def is_huiwen(s):
    return "是" if s == s[::-1] else "不是"


input_str = input("输入一个字符串(判断是否是回文)")
print(f"输入的 \'{input_str}\' {is_huiwen(input_str)}回文")
