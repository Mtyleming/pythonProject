# 学生信息管理系统
# 
# 需求：使用字典存储学生信息
# 思路：1) 创建字典存储学生信息 2) 实现增删改查功能 3) 使用循环展示菜单
# {"胡晏铭":{"age":25,"skill":"java"}}
student = {}

print("欢迎使用学生信息管理系统")
while True:
    print("""
    #########学生信息管理系统###########
    #      1.添加学生
    #      2.修改学生
    #      3.删除学生
    #      4.查询指定学生
    #      5.查询所有学生 
    #      6.退出购物车
    ############################
    """)
    choice = int(input("请输入要执行的操作"))
    match choice:
        case 1:
            name = input("请输入学生姓名")
            ##如果存在
            if name in student:
                print("当前学生存在!请重新选择操作")
            else:
                age = int(input("请输入学生年龄"))
                skill = input("请输入学生技能")
                student[name] = {"age": age, "skill": skill}
                print("添加成功")
        case 2:
            name = input("请输入学生名称")
            if name not in student:
                print("当前学生不存在!请重新选择操作")
            else:
                age = int(input("请输入学生年龄"))
                skill = input("请输入学生技能")
                student[name] = {"age": age, "skill": skill}

        case 3:
            name = input("请输入学生名称")
            if name not in student:
                print("当前学生不存在!请重新选择操作")
            else:
                student.pop(name)
        case 4:
            name = input("请输入学生名称")
            if name not in student.keys():
                print("当前学生不存在!请重新选择操作")
            else:
                info = student[name]
                print(f"名称:{name} \t age:{info["age"]} \t skill:{info["skill"]}")
        case 5:
            for k in student.keys():
                info = student[k]
                print(f"名称:{k} \t age:{info["age"]} \t skill:{info["skill"]}")
        case 6:
            break
        case _:
            print("非法输入!")
