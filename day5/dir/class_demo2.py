class Student:
    name = "默认"
    def __init__(self, name):
        self.name = name



s = Student("张三")
s.age = 20  # ✅ 动态添加属性，Java 做不到
s.email = "zhang@test.com"  # ✅ 随时添加
del s.name
print(s.__dict__)
print(s.__str__())
print(s.name)
