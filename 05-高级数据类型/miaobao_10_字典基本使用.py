student_dict = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.78,
            "weight": 60}

# 取值
print(student_dict["name"])  # 取值的时候如果指定的key不存在则报错

# 增加/修改
# 键不存在则新增键值对，键存在则修改键值对
student_dict["number"] = 123456
student_dict["name"] = "大明"

# 删除
student_dict.pop("gender")  # 删除的时候如果指定的key不存在则报错

# 统计键值对数量
print(len(student_dict))

# 合并字典
temp_dict = {"身份证":330802,
             "age":20}  # 若合并字典中包含已经存在的键值对，则覆盖原有的键值对
student_dict.update(temp_dict)

print(student_dict)

# 清空字典
student_dict.clear()
print(student_dict)
