import json  # 导入json库
from colorama import Fore, Style  # 导入colorama库中的Fore和Style模块
import os  # 导入os库


class Student:  # 定义学生类
    def __init__(self, student_id, name, age, grade):  # 初始化学生类
        self.id = student_id  # 学生ID
        self.name = name  # 学生姓名
        self.age = age  # 学生年龄
        self.grade = grade  # 学生成绩

    @classmethod
    def from_dict(cls, data):  # 从字典创建学生对象
        return cls(
            student_id=data.get('id'),  # 获取学生ID
            name=data.get('name'),  # 获取学生姓名
            age=data.get('age'),  # 获取学生年龄
            grade=data.get('grade')  # 获取学生成绩
        )
