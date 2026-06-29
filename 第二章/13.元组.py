# t = (1,2,3,4,5,6,7,8,9)
# print(t)
# print(type(t))
#
#
# print(t.index(8))
# ##tt = tuple(1,) tuple(1) (1) 都报错
# tt = (1,)
# print(tt)
#
#
# # ------------------------------组包&解包-----------------------
# t1 = (1,2,3,4,5,6,7,8,9)
# t2 = 1,2,3,4
#
# #a,b,c,*d = t2
# #*a,b,c,d = t1
# #a,*b,c=t1
#
# # a = 10
# # b = 20
# # a,b = b,a
# a = 10
# b = 20
# c = 30
# b,c,a = a,b,c
import cmath

student = (
    ("S001","王林",89,85,70),
    ("S002","李四",90,95,65),
    ("S003","王麻子",59,56,90),
    ("S004","麦晓雯",75,77,68),
    ("S005","露娜",66,59,78)

)

#获取各科成绩
chinese = sorted([s[2] for s in student])
print(chinese[0])
print(min([s[2] for s in student]))
print(max([s[2] for s in student]))
print(sum([s[2] for s in student])/len(student))

map = [(s[1],round((s[2]+s[3]+s[4])/3,1)) for s in student]
print(map)
print( [i[0] for i in map if i[1] > 80])

for id,name,chineseScore,mathScore,englishScore in student:
    total = chineseScore + mathScore + englishScore
    avg = round(total/3,1)
    if avg > 80:
        print(f"{name},平均成绩{avg}")


