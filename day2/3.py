##########猜数字游戏(0-100)
import random


num = random.randint(1, 100)

# num = random.random()*100
# print(num)
# print(int(num))
# num = int(num)

inputNum = int(input("输入一个数字(0-100): "))
low = 0
up = 100
while inputNum != num:
    if inputNum > num:
        print("输入的数字过大")
        up = inputNum
        inputNum = int(input(f"输入一个数字({low}-{inputNum}): "))
    elif inputNum < num:
        print("输入数字过小")
        low = inputNum
        inputNum = int(input(f"输入一个数字({inputNum}-{up}): "))
else:
    print("恭喜恭喜")
