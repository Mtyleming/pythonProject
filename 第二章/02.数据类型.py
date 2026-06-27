#########初始金额10000
#####输入密码


initAmount = 10000
initPassword = "123456"

password = input("请输入密码")
if password != initPassword:
    print("密码错误")
    exit()
else:
    amount = int(input(f"您现在有{initAmount} 请输入取款金额:"))
    print(f"取钱后剩余金额为{initAmount - amount}")