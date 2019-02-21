#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import cards_tools

while True:
    # TODO(喵宝) 显示功能菜单
    cards_tools.show_menu()


    action_str = input("请选择希望执行的操作：")
    print("你选择的操作是【%s】" % action_str)

    if action_str in ["1", "2", "3"]:     # 1 2 3 针对名片的操作
        if action_str == "1":
            cards_tools.new_card()
        elif action_str == "2":
            cards_tools.show_all()
        elif action_str == "3":
            cards_tools.search_card()
        pass                              # 开发中不希望立即编写分支内容，可以用pass关键字
    elif action_str == "0":              # 0 退出系统
        print("欢迎再次使用名片管理系统")
        break
    else:                               # 其他内容表示输入错误，需要提示用户
        print("输入不正确，请重新选择")

