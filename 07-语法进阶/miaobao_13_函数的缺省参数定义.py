def print_info(name,gender=True):
    """

    :param name:  姓名
    :param gender:  True 男生， False 女生
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name,gender_text))


# 假设班上男生居多，默认gender为True
# 提示：指定缺省参数默认值时，应该使用最常见的值作为默认值
print_info("喵宝")
print_info("小美", False)