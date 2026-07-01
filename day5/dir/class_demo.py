class Student:
    # 类变量（类似 Java static 变量）
    school = "北京大学"

    # 构造器（类似 Java 构造方法）
    def __init__(self, name: str, age: int):
        # 实例变量（类似 Java 成员变量）
        self.name = name
        self.age = age

    # 实例方法（类似 Java 普通方法）
    def introduce(self):
        print(f"我叫{self.name}，今年{self.age}岁")

    # 类方法（类似 Java static 方法）
    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    # 静态方法（和 Java static 方法一样）
    @staticmethod
    def is_adult(age):
        return age >= 18
