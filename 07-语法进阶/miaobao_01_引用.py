def test(num):
    print("在函数内部%d对应的内存地址是%d" % (num, id(num)))

    result = "hello"
    print("函数返回数据的内存地址是%d" % id(result))

    # 函数的返回值返回的也是变量的引用，而不是值
    return result

a = 10

print("a变量保存的数据的内存地址是%d" % id(a))

# 调用test函数，本质是上传递是实参保存数据的引用，而不是实参保存数据的值
r = test(a)

print("%s 的内存地址是%d" % (r, id(r)))