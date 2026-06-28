# list = [11,22,55,33,44,0]
# for item in list:
#     print(item,end="\t")
#
# print()
# for i in range(0,len(list)):
#     print(list[i],end="\t")




#########list 案例1
# numList = []
# print("输入5个整数")
# for i in range(5):
#     numList.append(int(input("请输入")))
#
# numList.sort()
#
# print(f"最大值:{numList[-1]},最小值:{numList[0]},平均值:{sum(numList)/len(numList)}")
# print(f"最大值:{max(numList)},最小值:{min(numList)},平均值:{sum(numList)/len(numList)}")


############list 案例3
list1 = []
for i in range(0,20,1):
    list1.append((i+1)**2)
print(list1)
print([(i+1)**2 for i in range(0, 20)])



list2 = [11,56,77,65,45,2,48]
list3 = []
for i in list2:
    if i % 2 == 0:
        list3.append(i**2)
print(list3)
print([i**2 for i in list2 if i % 2 == 0])



nums = [3, 1, 2, 3, 2, 4]

# 无序去重
print(list(set(nums)))            # [1, 2, 3, 4]（可能）

# 保序去重
print(list(dict.fromkeys(nums)))  # [3, 1, 2, 4]（保持第一次出现的顺序）