"""
该代码的功能如下：

    获取当前目录的路径。
    打印当前目录下的所有文件名。
    提示用户输入待处理的数据文本名。
    读取数据文本文件，并将非空行且不以'#'开头的行解析为数据，并存储到data列表中。
    打印所有列的数据。
    按照第一列的数值递增顺序对数据进行排序，并打印排序后的第一列和对应的倒数第二列数据。
    计算每一行中第一列和倒数第二列数值的乘积，并对所有行的乘积求和。
    打印求和结果。

总体而言，该代码实现了以下功能：

    获取当前目录下的文件列表，并输出文件名。
    读取指定的数据文本文件，并解析其中的数据。
    打印数据的所有列。
    对数据按照第一列的数值进行排序，并输出排序后的第一列和对应的倒数第二列数据。
    计算数据中每一行的第一列和倒数第二列的乘积，并对所有行的乘积求和。
    输出求和结果。
"""


import os

# 获取当前目录
current_directory = os.getcwd()

# 打印同级目录下的所有文件
print("同级目录下的文件：")
for file_name in os.listdir(current_directory):
    if os.path.isfile(os.path.join(current_directory, file_name)):
        print(file_name)

# 提示用户输入待处理的数据文本名
data_file = input("请输入待处理的数据文本名：")

# 读取数据文本，忽略空行和#开头的行
data = []
with open(data_file, 'r') as file:
    for line in file:
        line = line.strip()
        if line != "" and not line.startswith("#"):
            data.append(line.split())

# 打印所有列的数据
print("所有列的数据：")
for row in data:
    print(row)

# 按照递增顺序打印第一列及其对应的倒数第二列数据
sorted_data = sorted(data, key=lambda x: float(x[0]))
print("按递增顺序打印第一列及其对应的倒数第二列数据：")
for row in sorted_data:
    print(row[0], row[-2])

# 计算每一行中的第一列和倒数第二列乘积的求和
sum_product = 0.0
for row in data:
    sum_product += float(row[0]) * float(row[-2])

# 打印求和结果
print("每一行中的第一列和倒数第二列乘积的求和：", sum_product)
