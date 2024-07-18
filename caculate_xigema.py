import math
import os
import pandas as pd
import numpy as np
import statistics
def caculate_pre_burn_period(folder_path,column_name, earlier_than,later_than):
    value=[]
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_excel(file_path)

            # 将'TIMESTAMP'列转换为日期时间类型
            df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
            # 删除早于earlier_than的行
            mask = (df['TIMESTAMP'] >= earlier_than) & (df['TIMESTAMP'] <= later_than)
            df_filtered = df[mask]

            # 将数据存储到数组中
            value.append(df_filtered[column_name].dropna().values)

    return value


def caculate_burn_period(folder_path,column_name, earlier_than,later_than):
    value=[]
    for filename in os.listdir(folder_path):
        if filename.endswith('4.xlsx'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_excel(file_path)

            # 将'TIMESTAMP'列转换为日期时间类型
            df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
            # 删除早于earlier_than的行
            mask = (df['TIMESTAMP'] >= earlier_than) & (df['TIMESTAMP'] <= later_than)
            df_filtered = df[mask]

            # 将数据存储到数组中
            value.append(df_filtered[column_name].dropna().values)

    return value

def caculate_post_burn_period(folder_path,column_name, earlier_than,later_than):
    value=[]
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_excel(file_path)

            # 将'TIMESTAMP'列转换为日期时间类型
            df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
            # 删除早于earlier_than的行
            mask = (df['TIMESTAMP'] >= earlier_than) & (df['TIMESTAMP'] <= later_than)
            df_filtered = df[mask]

            # 将数据存储到数组中
            value.append(df_filtered[column_name].dropna().values)

    return value

def list_std_dev(lst):
    # 将二维列表展平为一维列表
    flattened_lst = [item for sublist in lst for item in sublist]
    # 计算均值
    median = statistics.median(flattened_lst)
    formatted_median = format(median, ".3f")
    # print("中位数为:", formatted_median)
    mean = sum(flattened_lst) / len(flattened_lst)
    print("均值为:",mean)

    # 计算每个元素与均值的差的平方
    squared_diff = [(x - mean) ** 2 for x in flattened_lst]
    # 计算方差
    variance = sum(squared_diff) / len(squared_diff)
    # 计算标准差
    std_dev = math.sqrt(variance)
    print("标准差:", std_dev)

    max_value = max (flattened_lst)
    # print("最大值:", max_value)
    # min_value = min(flattened_lst)
    # print("最小值:", min_value)
    return std_dev,mean


# # 指定要读取的文件夹路径
folder_path = "D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn11_Sonic\\per_minute"
# 调用函数读取CSV文件并将数据存储到数组中
earlier_than = pd.Timestamp('2018-05-11 09:32:03')
later_than = pd.Timestamp('2018-05-11 09:42:03')
value= caculate_pre_burn_period(folder_path,'V_W',earlier_than,later_than)
list_std_dev(value)

print("*****burn*****")
earlier_than = pd.Timestamp('2018-05-11 09:42:26.2')
later_than = pd.Timestamp('2018-05-11 09:59:35.9')
value_burn = caculate_burn_period(folder_path,'V_W',earlier_than,later_than)
list_std_dev(value_burn)

print("*****post-burn*****")
earlier_than = pd.Timestamp('2018-05-11 09:59:35.9')
later_than = pd.Timestamp('2018-05-11 10:09:35.9')
value_post_burn = caculate_post_burn_period(folder_path,'V_W',earlier_than,later_than)
list_std_dev(value_post_burn)



