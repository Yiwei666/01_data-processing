# 01_data-processing
 Some Data Processing Scripts for Molecular Dynamics Simulations
 
56_isaacs_order.py

上述代码实现了以下功能：
    首先，代码列出了同级目录下的所有文件，并将它们打印出来，以便用户知道可以选择哪个数据文本文件进行处理。
    然后，代码提示用户输入待处理的数据文本名，并读取该文本文件的内容。
    在读取文本文件时，代码会忽略空行和以 '#' 开头的行，以确保只处理有效的数据行。
    接下来，代码打印了所有列的数据。它将每一行分割成不同的列，并将每列的数据打印出来。
    最后，代码按照第一列数据的递增顺序对数据进行排序，并打印出第一列及其对应的倒数第二列的数据。它首先将数据解析成列，然后根据第一列的值进行排序，并将排序后的结果打印出来。
通过这些步骤，代码可以处理指定数据文本文件中的数据，并提供了打印所有列数据以及按照第一列排序的功能。



57_isaacs[sum]_order.py

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

58_神经网络拟合配位数.py




59_[提升精度]神经网络拟合配位数曲线.py
