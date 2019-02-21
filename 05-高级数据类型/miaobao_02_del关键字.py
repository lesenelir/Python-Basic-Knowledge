name_list = ["张三", "李四", "王五"]
# 提示：日常开发中，从列表删除数据，建议使用列表提供的方法
del name_list[1]

# del 关键字的本质就是用将一个关键字将内存中删除
name = "小明"
del name

print(name_list)