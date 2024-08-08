import json
import os

from student import Student  # 导入学生类


class StudentManager:  # 定义学生管理类
    def __init__(self):  # 初始化学生管理类
        self.students = []  # 学生列表

    def add_student(self, student):  # 添加学生方法
        self.students.append(student)  # 将学生添加到列表中
        return "学生添加成功。"  # 返回成功信息

    def delete_student(self, student_id):  # 删除学生方法
        self.students = [s for s in self.students if s.id != student_id]  # 根据ID删除学生
        return "学生删除成功。"  # 返回成功信息

    def update_student(self, student_id, name=None, age=None, grade=None):  # 更新学生信息方法
        for student in self.students:  # 遍历学生列表
            if student.id == student_id:  # 找到匹配的学生ID
                if name:  # 如果提供了新姓名
                    student.name = name  # 更新姓名
                if age:  # 如果提供了新年龄
                    student.age = age  # 更新年龄
                if grade:  # 如果提供了新成绩
                    student.grade = grade  # 更新成绩
        return "学生信息更新成功。"  # 返回成功信息

    def view_students(self):  # 查看所有学生方法
        for student in self.students:  # 遍历学生列表
            print(f"ID: {student.id}, Name: {student.name}, Age: {student.age}, Grade: {student.grade}")  # 打印学生信息
        return "学生信息显示成功。"  # 返回成功信息

    def save_to_file(self, filename):  # 保存学生信息到文件方法
        with open(filename, 'w') as file:  # 打开文件写入模式
            json.dump([s.__dict__ for s in self.students], file)  # 将学生信息转换为字典并写入文件
        return "学生信息保存成功。"  # 返回成功信息

    def load_from_file(self, filename):  # 从文件加载学生信息方法
        if not os.path.exists(filename):  # 检查文件是否存在
            return "文件不存在，请检查文件名。"  # 提示文件不存在
        try:
            with open(filename, 'r') as file:  # 打开文件读取模式
                students = json.load(file)  # 读取文件内容
                self.students = [Student.from_dict(s) for s in students]  # 将读取的内容转换为学生对象并存入列表
            return "学生信息加载成功。"  # 返回成功信息
        except Exception as e:
            return f"读取文件时出错: {e}"  # 提示读取文件时出错
