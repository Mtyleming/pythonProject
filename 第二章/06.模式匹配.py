########类似于java的switch case

day = int(input("输入1-7 返回对应的星期中文"))
day_dict = {
    1: "星期一",
    2: "星期二",
    3: "星期三",
    4: "星期四",
    5: "星期五",
    6: "星期六",
    7: "星期天"
}

print(f"今天是星期{day_dict[day]}")

match day:
    case 1:
        print("今天是星期一")
    case 2:
        print("今天是星期二")
