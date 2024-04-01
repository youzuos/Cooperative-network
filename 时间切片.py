import pandas as pd

# 读取原始CSV文件
df = pd.read_csv("带时间序列的连边_修改.csv")

# 将“申请日”列转换为日期时间格式
df['start_time'] = pd.to_datetime(df['start_time'])

# 提取每一年的数据并保存到相应的CSV文件中
for year in range(df['start_time'].dt.year.min(), df['start_time'].dt.year.max() + 1):
    year_df = df[df['start_time'].dt.year == year]
    year_df.to_csv(f"{year}年边表.csv", index=False,encoding='utf-8-sig')