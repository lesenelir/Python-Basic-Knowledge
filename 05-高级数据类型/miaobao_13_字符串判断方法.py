
# 1. 判断空白字符
space_str = "  \t  \n   \r      "
print(space_str.isspace())

# 2. 判断字符串中方是否只包含数字
# NOTE: 都不能判断小数
num_str = "1"
print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())      # 可判断unicode
print(num_str.isnumeric())    # 可判断中文的数字

