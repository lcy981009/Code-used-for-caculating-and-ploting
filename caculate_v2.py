import os
import pandas as pd
from math import sqrt
import statistics
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
def calculate_variance(input_file, output_file,mean_streamwise,mean_cross_stream,mean_T,mean_w):
    # 读取 Excel 文件
    df = pd.read_excel(input_file)

    # 将 TIMESTAMP 列转换为 datetime 类型
    df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])

    # 将 TIMESTAMP 列设置为索引
    df.set_index('TIMESTAMP', inplace=True)
    df['streamwise'] -= mean_streamwise
    variance_streamwise = ((df['streamwise'] ** 2).resample('1T').mean())/2

    df['cross_stream']-=mean_cross_stream
    variance_cross_stream = ((df['cross_stream'] ** 2).resample('1T').mean())/2

    df['W']-=mean_w
    variance_W = ((df['W'] ** 2).resample('1T').mean())/2

    df['T']-=mean_T
    heat_flux=(df['T']*df['W']).resample('1T').mean()

    U_W=(df['streamwise']*df['W']).resample('1T').mean()
    V_W=(df['cross_stream']*df['W']).resample('1T').mean()

    friction_velocity=(U_W ** 2 + V_W ** 2).apply(sqrt)

    TKE=variance_streamwise+variance_cross_stream+variance_W


    # 创建新的 DataFrame 存储结果
    result_df = pd.DataFrame({
        'TIMESTAMP': variance_streamwise.index,  # 时间列
        'U_2': variance_streamwise.values ,
        'V_2':variance_cross_stream,
        'W_2':variance_W,
        'TKE':TKE,
        'U_W':U_W,
        'V_W':V_W,
        'U*2':friction_velocity,
        'heat_flux':heat_flux
    })


    # 将结果写入新的 Excel 文件
    result_df.to_excel(output_file, index=False)


def calculate_variance_in_folder(folder_path,folder_path_1,mean_streamwise,mean_cross_stream,mean_T,mean_W):
    # 列出指定文件夹中的所有文件
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.xlsx')]

    # 遍历文件夹中的每个文件
    for file in files:
        input_file = os.path.join(folder_path, file)
        output_file = os.path.join(folder_path_1, f"per_minute_{file}")  # 输出文件名加上前缀

        # 对每个文件执行计算方差的操作
        calculate_variance(input_file, output_file,mean_streamwise,mean_cross_stream,mean_T,mean_W)
        print(f"已经对 {file} 中的数据计算方差，并将结果保存到 {output_file} 中。")



folder_path =  "D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn20_Sonic"
folder_path_1 =  "D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn20_Sonic\\per_minute"
value_streamwise=read_csv_files_in_folder(folder_path,'streamwise')
std_dev_streamwise,mean_streamwise,median_streamwise=list_std_dev(value_streamwise,'streamwise')

value_cross_stream=read_csv_files_in_folder(folder_path,'cross_stream')
std_dev_cross_stream,mean_cross_stream,median_cross_stream=list_std_dev(value_cross_stream,'cross_stream')

value_T=read_csv_files_in_folder(folder_path,'T')
std_dev_T,mean_T,median_T=list_std_dev(value_T,'T')

value_W=read_csv_files_in_folder(folder_path,'W')
std_dev_W,mean_W,median_W=list_std_dev(value_W,'W')


calculate_variance_in_folder(folder_path,folder_path_1,mean_streamwise,mean_cross_stream,mean_T,mean_W)#mean_streamwise,mean_cross_stream,mean_T,mean_w
