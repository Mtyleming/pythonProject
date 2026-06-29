#选修足球学生名单
football_set ={"王林","曾牛","徐立国","遁天","天运子","韩立","厉飞雨","乌丑","紫灵"}
#选修篮球学生名单
basketball_set ={"张铁","墨居仁","王林","姜老道","曾牛","王蝉","韩立","天运子","李化元","厉飞雨","云露"}
#选修法语学生名单
french_set={"许木","王卓","十三","虎咆","姜老道","天运子","红蝶","厉飞雨","韩立","曾牛"}
# 选修艺术学生名单
art_set={"遁天","天运子","韩立","虎咆","姜老道","紫灵"}

#取交集拿出所有学生名单
dict1 = {}
student = french_set|basketball_set|french_set|art_set
for i,item in enumerate(student):
    num = 0
    if item in football_set:
        num += 1
    if item in basketball_set:
        num += 1
    if item in french_set:
        num += 1
    if item in art_set:
        num += 1
    dict1[item] = num
print(dict1)

print([football_set, basketball_set, french_set, art_set])

all_courses = [football_set, basketball_set, french_set, art_set]

# 取并集：所有学生
all_students = football_set | basketball_set | french_set | art_set
# 并集| 交集& 差集-
# 一行统计每个学生的选课数
result = [(student, sum(student in course for course in all_courses)) for student in all_students]
