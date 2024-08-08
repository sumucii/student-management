from student import Student
from student_manager import StudentManager  # 导入学生管理类
from colorama import Fore, Style  # 导入colorama库中的Fore和Style模块


def main():  # 主函数
    manager = StudentManager()  # 创建学生管理对象
    while True:  # 无限循环
        print(Fore.GREEN + "\n" + "*" * 20 + "学生管理系统" + "*" * 20 + Style.RESET_ALL)  # 打印标题

        print(
            Fore.YELLOW + "\n1. 添加学生\n2. 删除学生\n3. 更新学生\n4. 查看所有学生\n5. 保存到文件\n6. 从文件加载\n7. 退出" + Style.RESET_ALL)  # 打印菜单

        print(Fore.LIGHTMAGENTA_EX + "提示: 请先从文件加载学生信息，然后再进行其他操作。" + Style.RESET_ALL)  # 打印先加载提示信息

        print(Fore.GREEN + "*" * 50 + Style.RESET_ALL)  # 打印分隔线

        choice = input(Fore.CYAN + "请输入你的选择: " + Style.RESET_ALL)  # 获取用户选择

        if choice == '1':  # 如果选择添加学生
            student_id = input(Fore.CYAN + "请输入ID: " + Style.RESET_ALL)  # 输入学生ID
            name = input(Fore.CYAN + "请输入姓名: " + Style.RESET_ALL)  # 输入学生姓名
            age = input(Fore.CYAN + "请输入年龄: " + Style.RESET_ALL)  # 输入学生年龄
            grade = input(Fore.CYAN + "请输入成绩: " + Style.RESET_ALL)  # 输入学生成绩
            print(manager.add_student(Student(student_id, name, int(age), grade)))  # 添加学生并显示成功信息

        elif choice == '2':  # 如果选择删除学生
            student_id = input(Fore.CYAN + "请输入要删除的学生ID: " + Style.RESET_ALL)  # 输入要删除的学生ID
            print(manager.delete_student(student_id))  # 删除学生并显示成功信息

        elif choice == '3':  # 如果选择更新学生信息
            student_id = input(Fore.CYAN + "请输入要更新的学生ID: " + Style.RESET_ALL)  # 输入要更新的学生ID
            name = input(Fore.CYAN + "请输入新姓名（留空跳过）: " + Style.RESET_ALL)  # 输入新姓名（可选）
            age = input(Fore.CYAN + "请输入新年龄（留空跳过）: " + Style.RESET_ALL)  # 输入新年龄（可选）
            grade = input(Fore.CYAN + "请输入新成绩（留空跳过）: " + Style.RESET_ALL)  # 输入新成绩（可选）
            print(manager.update_student(student_id, name if name else None, int(age) if age else None,
                                         grade if grade else None))  # 更新学生信息并显示成功信息

        elif choice == '4':  # 如果选择查看所有学生
            print(manager.view_students())  # 查看所有学生并显示成功信息

        elif choice == '5':  # 如果选择保存到文件
            filename = input(Fore.CYAN + "请输入要保存的文件名: " + Style.RESET_ALL)  # 输入文件名
            print(manager.save_to_file(filename))  # 保存学生信息到文件并显示成功信息

        elif choice == '6':  # 如果选择从文件加载
            filename = input(Fore.CYAN + "请输入要加载的文件名: " + Style.RESET_ALL)  # 输入文件名
            print(manager.load_from_file(filename))  # 从文件加载学生信息并显示成功信息

        elif choice == '7':  # 如果选择退出
            break  # 退出循环

        else:  # 如果选择无效
            print(Fore.RED + "无效选择，请重试。" + Style.RESET_ALL)  # 提示无效选择

    print(Fore.GREEN + "谢谢使用，再见！" + Style.RESET_ALL)  # 打印再见信息


if __name__ == "__main__":  # 如果是主程序
    main()  # 调用主函数
