import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import rcParams
import numpy as np
import os
import pandas as pd

# 设置全局字体为 Times New Roman
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']
rcParams['font.size'] = 20

# 设置颜色（RGB值）
colors = [(46/255, 75/255, 160/255), (186/255, 62/255, 69/255), (26/255, 8/255, 25/255), (250/255, 164/255, 25/255)]
# 设置标记符号
markers = ['o', 'D', '*', 'P']

# 读取 Excel 文件
df1 = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_A1.xlsx")
# 将 TIMESTAMP 列转换为 datetime 类型，确保数据正确排序
df1['TIMESTAMP'] = pd.to_datetime(df1['TIMESTAMP'])
# 设置 TIMESTAMP 列为索引
df1.set_index('TIMESTAMP', inplace=True)

# 创建一个大画布，包含 16 张子图
fig, axs = plt.subplots(4, 4, figsize=(24, 16))
U_2 = df1['U_2']
V_2 = df1['V_2']
W_2 = df1['W_2']
TKE = df1['TKE']

timestamp1 = pd.Timestamp('2018-03-17 12:42:40.5')#burn开始时间
timestamp2 = pd.Timestamp('2018-03-17 12:52:05.5')#burn结束时间
# 绘制第一张子图（第一行第一列）
ax = axs[0, 0]
ax.plot(df1.index,U_2, color=colors[0], marker=markers[0],markersize=6,  label = r"$\mathrm{\mathit{u}'^2/2}$")  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df1.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label = r"$\mathrm{\mathit{v}'^2/2}$")  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df1.index,W_2, color=colors[2], marker=markers[2], markersize=8,label = r"$\mathrm{\mathit{w}'^2/2}$")  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df1.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label = r"$\mathrm{TKE}$")  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df1.index.min(), df1.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df1.index[3], ax.get_ylim()[1]*0.85, 'A1', fontsize=20, color='black')

ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.78)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.78)
ax.text(timestamp1, ax.get_ylim()[1]*0.5, '12:42:40.5', color='green', rotation=90, ha='right')#burn开始时间
ax.text(timestamp2, ax.get_ylim()[1]*0.5, '12:52:05.5', color='green', rotation=90, ha='right')#burn结束时间
ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True, labeltop=False)
plt.setp(ax.get_xticklabels(), visible=False)
#第二张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_A2.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[0, 1]
ax.plot(df1.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df1.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df1.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df1.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df.index.min(), df.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'A2', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True, labeltop=False)
ax.tick_params(axis='y', which='both', left=True, right=False, labelleft=False, labelright=False)
plt.setp(ax.get_xticklabels(), visible=False)
#第三张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_A3.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[0, 2]
ax.plot(df1.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df1.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df1.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df1.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df.index.min(), df.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'A3', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True, labeltop=False)
ax.tick_params(axis='y', which='both', left=True, right=False, labelleft=False, labelright=False)
plt.setp(ax.get_xticklabels(), visible=False)
#第四张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_A4.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[0, 3]
ax.plot(df1.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df1.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df1.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df1.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df.index.min(), df.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'A4', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True, labeltop=False)
ax.tick_params(axis='y', which='both', left=True, right=False, labelleft=False, labelright=False)
plt.setp(ax.get_xticklabels(), visible=False)

#第5张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_B1.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[1, 0]
ax.plot(df1.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df1.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df1.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df1.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df.index.min(), df.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'B1', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True, labeltop=False)
plt.setp(ax.get_xticklabels(), visible=False)

#第6张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_B2.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[1, 1]
ax.plot(df1.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df1.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df1.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df1.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df.index.min(), df.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'B2', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True, labeltop=False)
ax.tick_params(axis='y', which='both', left=True, right=False, labelleft=False, labelright=False)
plt.setp(ax.get_xticklabels(), visible=False)
#第7张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_B3.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[1, 2]
ax.plot(df1.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df1.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df1.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df1.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df.index.min(), df.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'B3', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True, labeltop=False)
ax.tick_params(axis='y', which='both', left=True, right=False, labelleft=False, labelright=False)
plt.setp(ax.get_xticklabels(), visible=False)


#第8张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_B4.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[1, 3]
ax.plot(df1.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df1.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df1.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df1.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df.index.min(), df.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'B4', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True, labeltop=False)
ax.tick_params(axis='y', which='both', left=True, right=False, labelleft=False, labelright=False)
plt.setp(ax.get_xticklabels(), visible=False)

#第9张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_C1.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[2, 0]
ax.plot(df1.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df1.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df1.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df1.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df.index.min(), df.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'C1', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True, labeltop=False)
plt.setp(ax.get_xticklabels(), visible=False)

#第10张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_C2.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[2, 1]
ax.plot(df1.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df1.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df1.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df1.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df.index.min(), df.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'C2', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True, labeltop=False)
ax.tick_params(axis='y', which='both', left=True, right=False, labelleft=False, labelright=False)
plt.setp(ax.get_xticklabels(), visible=False)

#第11张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_C3.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[2, 2]
ax.plot(df1.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df1.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df1.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df1.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df.index.min(), df.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'C3', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True, labeltop=False)
ax.tick_params(axis='y', which='both', left=True, right=False, labelleft=False, labelright=False)
plt.setp(ax.get_xticklabels(), visible=False)

#第12张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_C4.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[2, 3]
ax.plot(df1.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df1.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df1.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df1.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df.index.min(), df.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'C4', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=True, labeltop=False)
ax.tick_params(axis='y', which='both', left=True, right=False, labelleft=False, labelright=False)
plt.setp(ax.get_xticklabels(), visible=False)

#第13张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_D1.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[3, 0]
ax.plot(df.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df1.index.min(), df1.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'D1', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.tick_params(axis='x', rotation=45,labelsize=20)
ax.get_xticklabels()[-1].set_color('white')
#第14张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_D2.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[3, 1]
ax.plot(df.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df1.index.min(), df1.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'D2', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.tick_params(axis='x', rotation=45,labelsize=20)
ax.get_xticklabels()[-1].set_color('white')
ax.tick_params(axis='y', which='both', left=True, right=False, labelleft=False, labelright=False)

#第15张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_D3.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[3, 2]
ax.plot(df.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df1.index.min(), df1.index.max()])
ax.set_ylim(-0.1, 3.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'D3', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.tick_params(axis='x', rotation=45,labelsize=20)
ax.get_xticklabels()[-1].set_color('white')
ax.tick_params(axis='y', which='both', left=True, right=False, labelleft=False, labelright=False)


#第16张子图
df = pd.read_excel("D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\per_minute\\per_minute_Burn05_Sonic_D4.xlsx")
df['TIMESTAMP'] = pd.to_datetime(df['TIMESTAMP'])
df.set_index('TIMESTAMP', inplace=True)
U_2 = df['U_2']
V_2 = df['V_2']
W_2 = df['W_2']
TKE = df['TKE']
ax = axs[3, 3]
ax.plot(df.index,U_2, color=colors[0], marker=markers[0],markersize=6, label='U_2')  # 绘制U_2，使用colors[0]颜色和markers[0]标记
ax.plot(df.index,V_2, color=colors[1], marker=markers[1],markersize=5.5, label='V_2')  # 绘制V_2，使用colors[1]颜色和markers[1]标记
ax.plot(df.index,W_2, color=colors[2], marker=markers[2], markersize=8,label='W_2')  # 绘制W_2，使用colors[2]颜色和markers[2]标记
ax.plot(df.index,TKE, color=colors[3], marker=markers[3],markersize=6.3, label='TKE')  # 绘制TKE，使用colors[3]颜色和markers[3]标记
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.set_xlim([df1.index.min(), df1.index.max()])
ax.set_ylim(-0.1, 5.1)
ax.set_yticks([0, 0.5, 1, 1.5, 2,2.5,3,3.5,4,4.5,5])
ax.text(df.index[3], ax.get_ylim()[1]*0.85, 'D4', fontsize=20, color='black')
ax.axvline(x=timestamp1, color='green', linestyle='--', linewidth=0.8)
ax.axvline(x=timestamp2, color='green', linestyle='--', linewidth=0.8)
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=5))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax.tick_params(axis='x', rotation=45,labelsize=20)
ax.get_xticklabels()[-1].set_color('white')
ax.tick_params(axis='y', which='both', left=True, right=False, labelleft=False, labelright=False)
plt.subplots_adjust(hspace=0.04)#表示每行之间的距离
plt.subplots_adjust(wspace=0.03)#表示每列之间的距离

# fig.suptitle('Temperature and Turbulent Fluxes Over Time')
axs[0,0].legend(prop={'size': 24},loc='upper center', bbox_to_anchor=(2, 1.3), shadow=True, ncol=4)



fig.text(0.5,0.05,'TIMESTAMP',fontsize=24,ha='center')
fig.text(0.08,0.5,'Kinetic Energy(m²/s²)',fontsize=24,va='center',rotation='vertical')
fig.savefig('D:\\湍流数据\\风速数据\\RDS-2022-0081_Data\\Data\\SERDP_10x10_Sonic_Raw\\Burn05_Sonic\\绘图\\TKE_Burn05.png', dpi=600, bbox_inches='tight')

plt.close(fig)
