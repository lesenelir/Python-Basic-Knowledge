name_list = ["zhangsan", "lisi", "wangwu"]

# 1.取值和取索引
print(name_list[2])              # 取值
print(name_list.index("lisi"))   # 取索引

# 2.修改
name_list[2] = "王五"
# name_list[3] = "王小二" 此语句会报错，列表指定的索引超出范围，程序会报错

# 3.增加
name_list.append("miaobao") # append方法在列表的末尾追加数据
name_list.insert(1,"小美")  # insert方法在列表的指定位置插入数据

temp_list = ["孙悟空","猪八戒", "沙师弟"]
name_list.extend(temp_list) # extend方法可以把其他列表的数据全部追加到当前列表的末尾

# 4.删除
name_list.remove("wangwu")  # remove方法可以把指定在列表的元素删除
name_list.pop()             # pop方法默认把列表中最后一个元素删除
name_list.pop(3)            # pop方法指定删除索引，即删除指定元素
name_list.clear()           # clear方法删除整个列表清空

print(name_list)

