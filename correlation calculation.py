import os
import pandas as pd
from scipy.stats import spearmanr

# 文件夹路径
folder_path = "D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn12_Sonic"

# 用于存储相关系数的列表
results = []
earlier_than = pd.Timestamp('2018-05-11 12:01:05')
later_than = pd.Timestamp('2018-05-11 12:28:48.4')
# 遍历文件夹中的每个xlsx文件
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        file_path = os.path.join(folder_path, filename)

        # 读取xlsx文件
        df = pd.read_excel(file_path)
        df['streamwise'] = df['streamwise'].diff().abs()
        df['cross_stream'] = df['cross_stream'].diff().abs()

        df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
        # 删除早于earlier_than的行
        mask = (df['TIMESTAMP'] >= earlier_than) & (df['TIMESTAMP'] <= later_than)
        df_filtered = df[mask]
        # 检查文件中是否包含'HWC', 'streamwise', 'cross_stream'三列
        required_columns = ['HWC', 'streamwise', 'cross_stream']
        if all(col in df_filtered.columns for col in required_columns):
            # 计算Spearman相关系数
            for col in ['streamwise', 'cross_stream']:
                spearman_corr, _ = spearmanr(df_filtered['HWC'], df_filtered[col])

                results.append(f"{filename}: Spearman correlation between HWC and {col}: {spearman_corr:.4f}")

# 将结果写入txt文件
output_file = "D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn12_Sonic\\Spearman.txt"
with open(output_file, 'w') as f:
    f.write("\n".join(results))

print(f"Results have been saved to {output_file}")
