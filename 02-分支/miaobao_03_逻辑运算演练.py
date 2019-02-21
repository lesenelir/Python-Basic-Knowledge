# 练习一
age = 120
if age >= 0 and age <= 120:
    print("年龄正确")
else:
    print("年龄不正确")

# 练习二
python_score = 80
c_score = 50
if python_score > 60 or c_score > 60:
    print("考试通过")
else:
    print("考试失败")

# 练习三
#开发中，通常希望某个条件不满足时，执行一些代码，可以使用not
#另外，如果需要拼接复杂的逻辑计算条件，同样也可能使用到not
is_employee = False
if not is_employee:
    print("不是本公司人员") #此处异常重要：not+False = True 此时循环条件已经为真就执行


