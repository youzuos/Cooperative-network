import pandas as pd

# 读取CSV文件，指定dtype为object，禁用内存优化，使用latin1编码
df = pd.read_csv("带时间序列的连边.csv", encoding="latin1", dtype=object, low_memory=False)

# 将start_time列转换为日期时间格式
df['start_time'] = pd.to_datetime(df['start_time'], format='%Y/%m/%d')

# 将end_time设置为每年的12月31日
df['end_time'] = df['start_time'].apply(lambda x: x.replace(month=12, day=31))

# 删除未命名的列
df = df.drop(columns=df.columns[df.columns.str.contains('Unnamed')])

# 将end_time列移动到第三列位置
end_time_col = df.pop('end_time')
df.insert(1, 'end_time', end_time_col)

# 保存修改后的数据到CSV文件，使用latin1编码
df.to_csv("带时间序列的连边_修改.csv", index=False, encoding="latin1")
