#输入温度
a = float(input("请输入摄氏温度："))
b = float(input("请输入华氏温度："))
#转换温度
c = a * 9/5 + 32
d = 5/9 * (b - 32)
print("摄氏温度{}转化为华氏温度为：{}".format(a,c))
print("华氏温度{}转化为摄氏温度为：{}".format(b,d))
