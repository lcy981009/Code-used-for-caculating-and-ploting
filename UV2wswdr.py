import os
import pandas as pd
import numpy as np
import math


# 第一步计算风速风向
def process_file(file_path):
    deg = 180.0 / np.pi
    rad = np.pi / 180.0
    # 读取xlsx文件
    df = pd.read_excel(file_path)

    # 获取U和V列的数据
    U = df['U'].tolist()  # 东西向分量
    V = df['V'].tolist()  # 南北向分量

    # 计算风速
    wind_speed = np.sqrt(np.array(U) ** 2 + np.array(V) ** 2)

    # 计算风向
    wind_direction = 180+np.arctan2(-np.array(U), -np.array(V)) * deg # 返回的是弧度值

    # 将计算结果写入新列
    df['ws'] = wind_speed
    df['wdr'] = wind_direction

    # 提取文件名
    file_name = os.path.basename(file_path)

    # 构造输出文件路径
    output_file = os.path.join("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn02_Sonic",  + file_name)  # 替换为输出文件夹路径

    # 将DataFrame写入xlsx文件
    df.to_excel(output_file, index=False)



# 定义要处理的文件夹路径
folder_path = "D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn02_Sonic" # 替换为文件夹路径

# 遍历文件夹中的所有文件
for file_name in os.listdir(folder_path):
    if file_name.endswith(".xlsx"):
        # 构造文件的完整路径
        file_path = os.path.join(folder_path, file_name)

        # 处理该文件
        process_file(file_path)

