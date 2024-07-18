# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# from matplotlib import rcParams
#
# rcParams['font.family'] = 'serif'
# rcParams['font.serif'] = ['Times New Roman']
# rcParams['font.size'] = 12
#
# # 读取 Excel 文件
# df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\Burn05_Sonic_C2.xlsx")
#
# # 将 TIMESTAMP 列转换为 datetime 类型，确保数据正确排序
# df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
#
# # 设置 TIMESTAMP 列为索引
# df.set_index('TIMESTAMP', inplace=True)
#
# # 创建画布和子图，设置更大的 figsize 和 dpi
# fig, ax = plt.subplots(figsize=(18, 6), dpi=600)
#
# # 绘制 HWC 列的折线图，使用蓝色 (RGB: 11, 12, 186)，实线样式，线宽为1
# ax.plot(df.index, df['HWC'], label='HWC', color=(11/255, 12/255, 186/255), linestyle='-', linewidth=0.3)
#
# # 绘制 vWC 列的折线图，使用红色 (RGB: 216, 30, 28)，实线样式，线宽为1
# ax.plot(df.index, df['vWC'], label='VWC', color=(216/255, 30/255, 28/255), linestyle='-', linewidth=0.3)
#
# # 设置图形标题和轴标签（可选）
# ax.set_title('Temperature and Turbulent Fluxes Over Time')
# ax.set_xlabel('Timestamp')
# ax.set_ylabel('Values')
#
# # 添加图例（可选）
# ax.legend(loc='best')
#
# # 设置 x 轴主要刻度以每十分钟显示一次日期
# ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=10))
# ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
#
# # 设置 x 轴标签旋转
# plt.xticks(rotation=45)
#
# # 紧凑布局，避免图形被遮挡
# plt.tight_layout()
#
# # 显示网格线，增加可读性
# plt.grid(True)
#
# # 添加竖直虚线，调整虚线间隔和线型
# timestamp1 = pd.Timestamp('2018-03-17 12:42:40.5')
# timestamp2 = pd.Timestamp('2018-03-17 12:52:05.5')
#
# ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.5)  # 调整虚线线宽为0.5
# ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.5)  # 调整虚线线宽为0.5
#
# # 在竖直虚线位置添加文本标签
# ax.text(timestamp1, ax.get_ylim()[1]*0.95, '2018-03-17 12:42:40.5', color='green', rotation=90, ha='right')
# ax.text(timestamp2, ax.get_ylim()[1]*0.95, '2018-03-17 12:52:05.5', color='green', rotation=90, ha='right')
#
# # 保存图形为文件，dpi 可以根据需要调整
# fig.savefig('D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\绘图\\VWC_C2.png', dpi=600, bbox_inches='tight')
#
# # 关闭图形对象，释放资源
# plt.close(fig)


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams


rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
rcParams['font.size'] = 20
# 读取Excel文件
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn02_Sonic\\per_minute\\per_minute_Burn02_Sonic_A1.xlsx")


# 提取数据列
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']

# 设置颜色（RGB值）
colors = [(46/255, 75/255, 160/255), (186/255, 62/255, 69/255), (26/255, 8/255, 25/255), (250/255, 164/255, 25/255)]

# 设置标记符号
markers = ['o', 'D', '*', 'P']

# 绘制点线图
plt.figure(figsize=(10, 6))  # 设置图像大小

plt.plot(U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
plt.plot(V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
plt.plot(W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
plt.plot(TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记

plt.xlabel('Index')  # 设置x轴标签
plt.ylabel('Values')  # 设置y轴标签
plt.title('Line Plot of U_2, V_2, W_2, TKE')  # 设置标题
plt.legend()  # 显示图例


plt.show()  # 显示图像
