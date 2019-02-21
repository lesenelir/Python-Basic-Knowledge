# for循环加入else语句一般的应用场景：
#   迭代遍历嵌套的数据类型

students = [
    {
        "name": "阿土"},
    {
        "name": "小美"}
]

find_name = "小美"


for stu_dict in students:
    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了%s" % find_name)
        # 如果找到了，应该直接退出循环，不再遍历后续元素
        break
else:    # 完整遍历完for循环才会执行else的语句
    print("抱歉，没有找到%s" % find_name)


print("循环结束")