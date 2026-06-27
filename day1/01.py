#######Hello world
import datetime

print("Hello World")

#######个人信息打印
name = "胡晏铭"
age = 25
dateTime = datetime.datetime.now().strftime("%Y-%m-%d")
print(dateTime, name, age)
print(dateTime + name + str(age))
print("今天是%s ,我是%s,今年%s岁" % (dateTime, name ,age))
print(f"今天是{dateTime} ,我是{name},今年{age}岁")

# #######变量交换
num1 = 1000
num2 = 2000

temp = num2
num2 = num1
num1 = temp
print("num1:", num1)
print("num2:", num2)

#######四则运算
print("请输入两个数字类型变量值:")
a = int(input("num1:"))
b = int(input("num2:"))
print(f"{a} + {b} =", a + b)
print(f"{a} - {b} =", a - b)
print(f"{a} * {b} =", a * b)
print(f"{a} / {b} =", a / b)
