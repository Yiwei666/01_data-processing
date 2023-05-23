"""
该代码的功能如下：

    导入所需的库：os、numpy、tensorflow。
    获取当前目录下的所有文件名，并打印出来。
    提示用户输入待处理的数据文本名。
    读取指定的数据文件，将非空且不以'@'开头的行解析为数据，并存储到data列表中。
    将数据拆分为输入列和输出列，分别存储在inputs和outputs的NumPy数组中。
    构建一个神经网络模型，该模型包括一个具有64个神经元的隐藏层，激活函数为ReLU，以及一个输出层。
    编译模型，指定优化器为Adam，损失函数为均方误差（Mean Squared Error）。
    使用输入数据和输出数据拟合（训练）模型，进行100个周期（epochs）的训练。
    提示用户输入一个数据。
    使用训练好的模型对输入数据进行预测。
    打印预测值。

总体而言，该代码实现了以下功能：

    读取指定的数据文件并解析成输入和输出数据。
    使用这些数据训练一个简单的神经网络模型。
    使用训练好的模型对用户提供的数据进行预测，并输出预测结果。
"""


import os
import numpy as np
import tensorflow as tf

# 获取同级目录下的所有文件
file_list = os.listdir('.')
# 打印所有文件名
for file_name in file_list:
    print(file_name)

# 提示用户输入待处理的数据文本名
data_file = input("请输入待处理的数据文本名: ")

# 读取数据文件
data = []
with open(data_file, 'r') as file:
    for line in file:
        line = line.strip()
        if line and not line.startswith('@'):
            data.append(line.split())

# 将数据拆分为输入和输出列
inputs = np.array([float(row[0]) for row in data])
outputs = np.array([float(row[1]) for row in data])

# 构建神经网络模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# 拟合模型
model.fit(inputs, outputs, epochs=100)

# 提示用户输入一个数据
input_data = float(input("请输入一个数据: "))

# 使用模型进行预测
prediction = model.predict(np.array([input_data]))

# 打印预测值
print("预测值:", prediction[0])
