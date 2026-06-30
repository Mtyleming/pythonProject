# 函数练习
#
# 需求：实现各种实用函数
# 思路：1) 实现计算函数（加减乘除）2) 实现字符串处理函数 3) 使用lambda简化代码

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
#
# def cal(a,b,oper):
#     return oper(a,b)
#
# num1 = int(input())
# num2 = int(input())
# print(f"{num1}+{num2}={cal(num1,num2,add)}")
# print(f"{num1}-{num2}={cal(num1,num2,sub)}")
# print(f"{num1}*{num2}={cal(num1,num2,mul)}")
# print(f"{num1}/{num2}={cal(num1,num2,div)}")
#
#
# print(f"{num1}+{num2}={cal(num1,num2,lambda a,b:a+b)}")
# print(f"{num1}-{num2}={cal(num1,num2,lambda a,b:a-b)}")
# print(f"{num1}*{num2}={cal(num1,num2,lambda a,b:a*b)}")
# print(f"{num1}/{num2}={cal(num1,num2,lambda a,b:a/b)}")

def str_fun(a,oper):
    return oper(a)

#####倒转
print(str_fun("abced",lambda x:x[::-1]))
#####拿出重复的字符
in_str = "abcedadwjpxjvehef"
print(str_fun(in_str,lambda x: set([i for i in x if in_str.count(i)>1])))

