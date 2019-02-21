# 函数处理参数个数不确定时，可以使用多值参数
# *接受元组，**接受字典

def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


demo(1)
demo(1, 2, 3, 4)
demo(1, 2, 3, 4, name="小明", age=18)
