import os
import pandas as pd
import numpy as np
import math
import statistics
from math import sqrt



def convert_csv_to_xlsx(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.csv'):
            csv_file_path = os.path.join(folder_path, filename)
            # 读取CSV文件
            df = pd.read_csv(csv_file_path)
            # 构造XLSX文件路径
            xlsx_file_path = os.path.splitext(csv_file_path)[0] + '.xlsx'
            # 将数据写入XLSX文件
            df.to_excel(xlsx_file_path, index=False)
def filter_timestamp_earlier(folder_path, earlier_than):
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_excel(file_path)

            # 将'TIMESTAMP'列转换为日期时间类型
            df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
            # 删除早于earlier_than的行
            df = df[df['TIMESTAMP'] >= earlier_than]
            # 删除含有NaN值的行
            df = df.dropna()
            # 删除DIAG列值不等于0的行
            df = df[df['DIAG'] == 0]
            # 删除指定范围外的行
            df = df[(df['T'] >= -50) & (df['T'] <= 50)]
            df = df[(df['U'] >= -40) & (df['U'] <= 40)]
            df = df[(df['V'] >= -40) & (df['V'] <= 40)]
            df = df[(df['W'] >= -40) & (df['W'] <= 40)]
            # 保存修改后的文件
            df.to_excel(file_path, index=False)


def wind_wdrcaculate(folder_path):
    """
    处理文件，计算风速和风向，并保存到原始文件
    """
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(folder_path, filename)
            deg = 180.0 / np.pi
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

            # 将DataFrame写回原始xlsx文件
            df.to_excel(file_path, index=False)

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
    print(f"{column_lable}标准差:",std_dev)

    return std_dev,mean, median

def wind_vector_projection(wind_speed, wind_direction, reference_direction):
    # 将风速和风向转换为笛卡尔坐标系中的矢量形式
    wind_vector_x = wind_speed * math.cos(math.radians(wind_direction))
    wind_vector_y = wind_speed * math.sin(math.radians(wind_direction))
    #print("x分量为:", wind_vector_x,"y分量为：",wind_vector_y)

    # 构建参考风向和垂直风向的单位矢量
    reference_unit_vector_x = math.cos(math.radians(reference_direction))
    reference_unit_vector_y = math.sin(math.radians(reference_direction))
    #print("x参考分量为:", reference_unit_vector_x, "y参考分量为：", reference_unit_vector_y)

    # 计算风矢量在参考风向上的投影
    projection_reference = (wind_vector_x * reference_unit_vector_x) + (wind_vector_y * reference_unit_vector_y)

    # 计算风矢量在垂直风向上的投影
    projection_vertical = -((wind_vector_x * -reference_unit_vector_y) + (wind_vector_y * reference_unit_vector_x))

    return projection_reference, projection_vertical


def projection(folder_path,mean_wdr):
    # 获取文件夹下所有xlsx文件的文件名
    files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

    for file in files:
        file_path = os.path.join(folder_path, file)
        # 读取Excel文件中的数据
        df = pd.read_excel(file_path, sheet_name='Sheet1')  # 假设数据在Sheet1中

        # 计算投影并将结果写入Sheet2
        projections = []
        for index, row in df.iterrows():
            wind_speed = row['ws']
            wind_direction = row['wdr']
            reference_direction = mean_wdr

            projection_reference, projection_vertical = wind_vector_projection(wind_speed, wind_direction,
                                                                               reference_direction)
            df['ws'] = wind_speed
            df['wdr'] = wind_direction

            projections.append({'streamwise': projection_reference, 'cross_stream': projection_vertical})

        # 将计算结果写入Sheet2
        df_projections = pd.DataFrame(projections)
        with pd.ExcelWriter(file_path, mode='a', engine='openpyxl') as writer:
            df_projections.to_excel(writer,sheet_name='Sheet2', index=False)

def merge_sheets_in_folder(folder_path, sheet1_name='Sheet1', sheet2_name='Sheet2', columns_to_merge=['Column1', 'Column2']):
    # List all files in the specified folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith('.xlsx')]

    # Iterate over each file in the folder
    for file in files:
        file_path = os.path.join(folder_path, file)

        # Read the Excel file with both sheets
        xls = pd.ExcelFile(file_path)

        # Read both sheets into separate dataframes
        sheet1_df = pd.read_excel(xls, sheet_name=sheet1_name)
        sheet2_df = pd.read_excel(xls, sheet_name=sheet2_name)

        # Merge the specified columns from sheet2 to sheet1
        for column in columns_to_merge:
            sheet1_df[column] = sheet2_df[column]

        # Write the modified sheet1 back to the Excel file
        with pd.ExcelWriter(file_path, mode='a', engine='openpyxl') as writer:
            # If 'Sheet1' already exists, delete it
            if sheet1_name in writer.book.sheetnames:
                writer.book.remove(writer.book[sheet1_name])
            sheet1_df.to_excel(writer, index=False, sheet_name=sheet1_name)

            if sheet2_name in writer.book.sheetnames:
                writer.book.remove(writer.book[sheet2_name])

        #print(f"Merged columns from {sheet2_name} to {sheet1_name} and updated {sheet1_name} in {file}.")

def calculate_Hwc(row):
    streamwise_diff = row['streamwise'].diff()  # 计算相邻时刻的 streamwise 差值
    cross_stream_diff = row['cross_stream'].diff(periods=1)  # 计算相邻两列 cross_stream 差值
    vwc_H = (streamwise_diff ** 2 + cross_stream_diff ** 2).apply(sqrt)  # 计算 VWC

    return vwc_H


def calculate_Vwc(row):
    W_diff = row['W'].diff()
    vwc_v = (W_diff ** 2 ).apply(sqrt)  # 计算 VWC

    return vwc_v
def calculate_s(row):
    S=(row['U']**2+row['V']**2).apply(sqrt)
    return S


def append_VWC_S(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_excel(file_path)

            df['HWC'] = calculate_Hwc(df)
            df['VWC'] = calculate_Vwc(df)
            df['S'] = calculate_s(df)

            df.to_excel(file_path, index=False)



def assign_quadrant_heat(row,mean_W,mean_T):
    if row['W'] > mean_W and row['T'] > mean_T:
        return 1
    elif row['W'] < mean_W and row['T'] > mean_T:
        return 2
    elif row['W'] < mean_W and row['T'] < mean_T:
        return 3
    elif row['W'] > mean_W and row['T'] < mean_T:
        return 4

def assign_quadrant_momentum(row,mean_W,mean_S):
    if row['W'] > mean_W and row['S'] > mean_S:
        return 1
    elif row['W'] < mean_W and row['S'] > mean_S:
        return 2
    elif row['W'] < mean_W and row['S'] < mean_S:
        return 3
    elif row['W'] > mean_W and row['S'] < mean_S:
        return 4

def quadrant_analyses(folder_path,mean_W,mean_T,mean_S):
    for filename in os.listdir(folder_path):
        if filename.endswith('.xlsx'):
            file_path = os.path.join(folder_path, filename)
            # 读取 Excel 文件
            df = pd.read_excel(file_path)
            # 将条件应用于每一行，并添加新列
            df['Quadrant1'] = df.apply(assign_quadrant_heat,args=(mean_W, mean_T), axis=1)
            df['Quadrant2'] = df.apply(assign_quadrant_momentum,args=(mean_W, mean_S), axis=1)
            # 将修改后的 DataFrame 保存回原文件
            df.to_excel(file_path, index=False)





# 文件夹路径
folder_path = "D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn20_Sonic"

# 热像仪首次检测到300℃的时间-10分钟
earlier_than = pd.Timestamp('2019-05-20 14:16:12')

#csv转xlsx
convert_csv_to_xlsx(folder_path)
# 删除超前行，检查异常值
filter_timestamp_earlier(folder_path, earlier_than)
#U V转风速风向
wind_wdrcaculate(folder_path)

#计算T的标准差及均值
value_T=read_csv_files_in_folder(folder_path,'T')

std_dev_T,mean_T,median_T=list_std_dev(value_T,'T')

#计算风向均值，中位数

value_wdr=read_csv_files_in_folder(folder_path,'wdr')

std_dev_wdr,mean_wdr,median_wdr = list_std_dev(value_wdr,'wdr')
#风速风向向顺流横流方向投影
projection(folder_path,mean_wdr)

merge_sheets_in_folder(folder_path, sheet1_name='Sheet1', sheet2_name='Sheet2', columns_to_merge=['streamwise', 'cross_stream'])

append_VWC_S(folder_path)

value_W=read_csv_files_in_folder(folder_path,'W')

std_dev_W,mean_W,median_W=list_std_dev(value_W,'W')

value_S=read_csv_files_in_folder(folder_path,'S')

std_dev_S,mean_S,median_S=list_std_dev(value_S,'S')

quadrant_analyses(folder_path,mean_W,mean_T,mean_S)

















