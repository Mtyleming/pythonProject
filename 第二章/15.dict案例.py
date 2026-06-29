########购物车系统#########

goods = {}

print("欢迎使用购物车系统")
while True:
    print("""
    #########购物车系统###########
    #      1.添加购物车
    #      2.修改购物车
    #      3.删除购物车
    #      4.查询制定商品
    #      5.查询购物车 
    #      6.退出购物车
    ############################
    """)
    choice = int(input("请输入要执行的操作"))

    match choice:
        case 1:
            goodsName = input("请输入商品名称")
            ##如果存在
            if goodsName in goods:
                print("当前商品存在!请重新选择操作")
            else:
                goodsPrice = float(input("请输入商品价格"))
                goodsNum = int(input("请输入商品数量"))
                goods[goodsName] = {"价格": goodsPrice, "数量": goodsNum}
                print("添加成功")
        case 2:
            goodsName = input("请输入商品名称")
            if goodsName not in goods:
                print("当前商品不存在!请重新选择操作")
            else:
                goodsPrice = float(input("请输入商品价格"))
                goodsNum = int(input("请输入商品数量"))
                goods[goodsName] = {"价格": goodsPrice, "数量": goodsNum}

        case 3:
            goodsName = input("请输入商品名称")
            if goodsName not in goods:
                print("当前商品不存在!请重新选择操作")
            else:
                goods.pop(goodsName)
        case 4:
            goodsName = input("请输入商品名称")
            # if goodsName not in goods:
            #     print("当前商品不存在!请重新选择操作")
            # else:
            #     print(f"名称:{goodsName} \t 价格:{goods[goodsName]["价格"]} \t 数量:{goods[goodsName]["数量"]}")
            if goodsName not in goods.keys():
                print("当前商品不存在!请重新选择操作")
            else:
                goodsInfo = goods[goodsName]
                print(f"名称:{goodsName} \t 价格:{goodsInfo["价格"]} \t 数量:{goodsInfo["数量"]}")
        case 5:
            for i in goods.keys():
                goodsInfo = goods[i]
                print(f"名称:{i} \t 价格:{goodsInfo["价格"]} \t 数量:{goodsInfo["数量"]}")
        case 6:
            break
        case _:
            print("非法输入!")
