########if条件判断练习
score = 685
if score >= 680:
    print(f"你可以上清华{score}")


########年份闰年判断 (非整百年 能被4除|| 整百年能被400整除)
year = int(input("输入年份判断年份是否是闰年"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}是闰年")
else:
    print(f"{year}是平年")
