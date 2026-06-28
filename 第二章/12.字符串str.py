s = "建工资质二级"

newstr = s[-2:]
newstr2 = s[-2:0]
print(newstr)
print(newstr2)

print(s.startswith("建工"))


address_str = input("请输入一个邮箱地址")
if address_str.count("@") == 1 and address_str.find(".") == 1:
    print(f"这个邮箱{address_str}是合法的")
else:
    print(f"这个邮箱{address_str}是非法的")
