def demo(num, num_list):
    print("函数内部的代码")

    # 在函数内部，针对参数使用赋值语句，修改局部变量的引用，不会修改到外部实参变量
    num = 10

    num_list = [1,2,3]

    print(num)
    print(num_list)
    print("函数执行完成")


gl_num = 9
gl_list = [4,5,6]
demo(gl_num,gl_list)
print(gl_num)
print(gl_list)