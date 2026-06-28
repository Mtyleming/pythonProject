###待办事项管理
#
# 需求：使用列表实现待办事项的增删查
# 思路：1) 创建空列表 2) 实现添加、删除、查看功能 3) 使用循环展示菜单


event_list = []
op = input("请输入操作 1添加 2删除 3查看")
while op in ["1","2","3"]:
    if op == "1":
        event_list.append(input("请输入你的待办事项"))
    elif op == "2":
        for i,item in enumerate(event_list):
            print(f"序号:{i+1}  内容:{item}")
        event_list.pop(int(input("请输入你要删除的代办序号(删除后会自动排序)"))-1)
    elif op == "3":
        for i,item in enumerate(event_list):
            print(f"序号:{i+1}  内容:{item}")
    op = input("请输入操作 1添加 2删除 3查看")
