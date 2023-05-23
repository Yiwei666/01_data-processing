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
