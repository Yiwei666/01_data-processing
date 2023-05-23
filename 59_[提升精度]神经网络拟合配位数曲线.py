"""
该代码的功能如下：

    导入所需的库：os、numpy、tensorflow和MinMaxScaler（来自sklearn.preprocessing）。
    获取当前目录下的所有文件名，并打印出来。
    提示用户输入待处理的数据文本名。
    读取指定的数据文件，将非空且不以'@'开头的行解析为数据，并存储到data列表中。
    将数据拆分为输入列和输出列，分别存储在inputs和outputs的NumPy数组中。
    进行数据预处理，使用MinMaxScaler将输入和输出数据进行归一化处理，并存储在inputs_scaled和outputs_scaled中。
    构建一个神经网络模型，该模型包括多个具有128个神经元的隐藏层，激活函数为ReLU，以及一个输出层。
    编译模型，指定优化器为Adam，损失函数为均方误差（Mean Squared Error）。
    使用归一化后的输入数据和输出数据拟合（训练）模型，进行500个周期（epochs）的训练，每个批次的大小为16。
    提示用户输入一个数据。
    对输入数据进行预处理，使用之前创建的MinMaxScaler将输入数据进行归一化处理。
    使用训练好的模型对归一化后的输入数据进行预测。
    将预测值反向转换为原始数据范围，使用之前创建的MinMaxScaler将归一化后的预测值转换为原始数据。
    打印预测值。

总体而言，该代码实现了以下功能：

    读取指定的数据文件并解析成输入和输出数据。
    使用归一化处理对输入和输出数据进行预处理。
    使用这些数据训练一个具有多个隐藏层的神经网络模型。
    使用训练好的模型对用户提供的数据进行预测，并将预测结果反向转换为原始数据范围后输出。
"""

import os
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

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

# 数据预处理
input_scaler = MinMaxScaler()
output_scaler = MinMaxScaler()
inputs_scaled = input_scaler.fit_transform(inputs.reshape(-1, 1))
outputs_scaled = output_scaler.fit_transform(outputs.reshape(-1, 1))

# 构建神经网络模型
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1)
])
model.compile(optimizer='adam', loss='mse')

# 拟合模型
model.fit(inputs_scaled, outputs_scaled, epochs=500, batch_size=16)

# 提示用户输入一个数据
input_data = float(input("请输入一个数据: "))

# 对输入数据进行预处理
input_data_scaled = input_scaler.transform([[input_data]])

# 使用模型进行预测
prediction_scaled = model.predict(input_data_scaled)

# 将预测值反向转换为原始数据范围
prediction = output_scaler.inverse_transform(prediction_scaled)

# 打印预测值
print("预测值:", prediction[0][0])
