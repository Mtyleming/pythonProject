#########判断三个边长能不能构成一个三角形 且返回是什么三角形
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

if a+b>c and a+c>b and b+c>a:
    if a == b and b == c:
        print("等边三角形")
    elif a == b or b == c or a == c:
        print("等腰三角形")
    else:
        print("普通三角形")