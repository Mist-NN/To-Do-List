class TodoList:
    # 初始化TodoList类的实例，创建一个空的待办事项列表
    def __init__(self):
        self.todos = []

    # 添加一个新任务到待办事项列表
    def add_task(self, task):
        self.todos.append(task)
        print(f"添加任务：{task}")  # 打印添加任务的信息

    # 从待办事项列表中删除一个任务
    def remove_task(self, task):
        if task in self.todos:
            self.todos.remove(task)
            print(f"已删除任务：{task}")  # 打印删除任务的信息
        else:
            print("任务未找到！")  # 如果任务不存在，打印提示信息

    # 显示当前所有的待办事项
    def show_tasks(self):
        if self.todos:
            print("待办事项列表：")
            for index, task in enumerate(self.todos, 1):
                print(f"{index}. {task}")  # 打印任务编号和描述
        else:
            print("待办事项列表为空。")  # 如果列表为空，打印提示信息

    # 标记一个任务为完成并从列表中移除
    def complete_task(self, number):
        if 0 < number <= len(self.todos):
            task = self.todos.pop(number-1)  # 根据索引移除任务
            print(f"任务已完成：{task}")  # 打印完成任务的信息
        else:
            print("无效的任务编号！")  # 如果索引无效，打印提示信息


def main():
    todo_list = TodoList()  # 创建TodoList类的实例
    while True:
        print("\n待办事项管理器")  # 打印程序标题
        print("1. 添加任务")
        print("2. 删除任务")
        print("3. 显示任务")
        print("4. 完成任务")
        print("5. 退出")
        choice = input("请输入选择：")  # 获取用户选择

        if choice == "1":
            task = input("请输入要添加的任务：")  # 获取要添加的任务
            todo_list.add_task(task)
        elif choice == "2":
            task = input("请输入要删除的任务：")  # 获取要删除的任务
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.show_tasks()  # 显示所有任务
        elif choice == "4":
            if todo_list.todos:
                todo_list.show_tasks()  # 显示所有任务
                number = int(input("请输入要完成的任务编号："))  # 获取要完成的任务编号
                todo_list.complete_task(number)
            else:
                print("待办事项列表为空。")  # 如果列表为空，打印提示信息
        elif choice == "5":
            print("正在退出...")  # 打印退出信息
            break  # 退出循环
        else:
            print("无效的选择，请重新输入。")  # 如果输入无效，打印提示信息


if __name__ == "__main__":
    main()  # 程序入口点