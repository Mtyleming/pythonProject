########教务系统#########
class studentClass:

    def __init__(self, name: str, math=0, chines=0, english=0):
        self.name = name
        self.math = math
        self.chines = chines
        self.english = english
    def __str__(self):
        return f"姓名:{self.name}\t数学成绩:{self.math}\t语文成绩{self.chines}\t英语成绩{self.english}"
    def update_score(self,math, chines, english):
        if math is not None:
            self.math = math
        if chines is not None:
            self.chines = chines
        if english is not None:
            self.english = english

class studentSystem:
    version_code = "1.0"
    auther_name = "hym"

    def __init__(self, student_dict=None):
        if student_dict is None:
            student_dict = {}
        self.student_dict = student_dict

    def add_student(self):
        """
        添加学生
        :param student:传入学生对象
        """
        name = input("请输入学生名称")
        ##如果存在
        name_list = [i for i in self.student_dict.keys()]
        if name in name_list:
            print("当前学生已存在!请重新选择操作")
        else:
            print("当前学生不存在,可以正常添加")
            math = int(input("请输入数学成绩"))
            chinese = int(input("请输入语文成绩"))
            english = int(input("请输入英语成绩"))
            self.student_dict[name] = studentClass(name, math, chinese, english)
            print("添加成功")

    def update_student(self):
        name = input("请输入学生名称")
        ##如果存在
        name_list = [i for i in self.student_dict.keys()]
        if name not in name_list:
            print("当前学生不存在!请重新选择操作")
        else:
            print("已找到当前学生,请修改成绩")
            math = int(input("请输入数学成绩"))
            chinese = int(input("请输入语文成绩"))
            english = int(input("请输入英语成绩"))
            self.student_dict[name].update_score(math, chinese, english)

    def get_student_by_name(self):
        name = input("请输入学生名称")
        ##如果存在
        name_list = [i for i in self.student_dict.keys()]
        if name not in name_list:
            print("当前学生不存在!请重新选择操作")
        else:
            student_obj = self.student_dict[name]
            print(f"学生信息为:{student_obj}")

    def get_all_student(self):
        for i in self.student_dict:
            print(self.student_dict[i])

    def delete_student(self):
        name = input("请输入学生名称")
        ##如果存在
        name_list = [i for i in self.student_dict.keys()]
        if name not in name_list:
            print("当前学生不存在!请重新选择操作")
        else:
            self.student_dict.pop(name)


    def run(self):
        print("欢迎使用教务系统")
        while True:
            print("""
                #########教务系统###########
                #      1.添加学生成绩
                #      2.修改学生成绩
                #      3.删除学生成绩
                #      4.查询某位学生的成绩
                #      5.查询学生成绩
                #      6.退出学生成绩
                ############################
                """)
            choice = int(input("请输入要执行的操作"))

            match choice:
                case 1:
                    self.add_student()
                case 2:
                    self.update_student()
                case 3:
                    self.delete_student()
                case 4:
                    self.get_student_by_name()
                case 5:
                    self.get_all_student()
                case 6:
                    break
                case _:
                    print("非法输入!")


if __name__ == '__main__':
    sys = studentSystem()
    sys.run()
