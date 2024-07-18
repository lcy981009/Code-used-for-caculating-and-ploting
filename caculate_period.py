

import os
import pandas as pd
import numpy as np
import  statistics
import math
def read_csv_files_in_folder(folder_path, column_name, max_rows=6000):

    value = []
    # 遍历指定文件夹下的所有文件
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)
            try:
                # 读取CSV文件
                df = pd.read_excel(file_path, usecols=[column_name], nrows=max_rows)
                # 将数据存储到数组中
                value.append(df[column_name].values)
            except Exception as e:
                print(f"Error reading file {file_name}: {e}")
    return value

def list_std_dev(lst,column_lable):
    # 将二维列表展平为一维列表
    flattened_lst = [item for sublist in lst for item in sublist]
    # 计算均值
    median = statistics.median(flattened_lst)

    print(f"{column_lable}中位数为:", median)
    mean = sum(flattened_lst) / len(flattened_lst)
    print(f"{column_lable}均值为:",mean)

    # 计算每个元素与均值的差的平方
    squared_diff = [(x - mean) ** 2 for x in flattened_lst]
    # 计算方差
    variance = sum(squared_diff) / len(squared_diff)
    # 计算标准差
    std_dev = math.sqrt(variance)

    return std_dev,mean, median

# 定义文件夹路径
folder_path = "D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn20_Sonic"  # 替换为包含xlsx文件的文件夹路径

def filter_timestamp2(folder_path, T_mean, std_dev_T):
    # 初始化最小和最大时刻
    min_timestamp = None
    max_timestamp = None

    # 遍历文件夹中的所有xlsx文件
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_excel(file_path)

            # 找到温度超过 T_mean + 8*std_dev_T 的时刻
            exceed_threshold = df[df['T'] > (T_mean + 8* std_dev_T)]

            # 找到最早和最晚的时刻
            earliest_time = exceed_threshold['TIMESTAMP'].min()
            latest_time = exceed_threshold['TIMESTAMP'].max()

            # 更新最小和最大时刻，确保不是 NaN 值
            if earliest_time is not pd.NaT:
                if min_timestamp is None or earliest_time < min_timestamp:
                    min_timestamp = earliest_time
            if latest_time is not pd.NaT:
                if max_timestamp is None or latest_time > max_timestamp:
                    max_timestamp = latest_time

    # 将最小和最大时刻写入到 txt 文件中
    with open("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn20_Sonic\\period.txt", "w") as result_file:
        if min_timestamp is not None:
            result_file.write(f"Earliest timestamp among all files exceeding T_mean + 8*std_dev_T: {min_timestamp}\n")
        else:
            result_file.write("No valid earliest timestamp found.\n")

        if max_timestamp is not None:
            result_file.write(f"Latest timestamp among all files exceeding T_mean + 8*std_dev_T: {max_timestamp}\n")
        else:
            result_file.write("No valid latest timestamp found.\n")

# 假设 T_mean 和 std_dev_T 是预先定义的均值和标准差
# 温度的标准差

value_T=read_csv_files_in_folder(folder_path,'T')

std_dev_T,mean_T,median_T=list_std_dev(value_T,'T')
# 调用函数
filter_timestamp2(folder_path, mean_T, std_dev_T)






