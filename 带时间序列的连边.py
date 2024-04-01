import pandas as pd
import itertools

# 读取 Excel 文件
df = pd.read_excel('所有数据提取0.xlsx')

# 获取时间序列和申请人名
a = df.iloc[:, 0]
time_series = df.iloc[:, 1]
b = df.iloc[:, 2]
c = df.iloc[:, 3]
d = df.iloc[:, 4]
e = df.iloc[:, 5]
f = df.iloc[:, 6]
g = df.iloc[:, 7]
h = df.iloc[:, 8]
i = df.iloc[:, 9]
applicants = df.iloc[:, 10:]

# 生成两两组合
pairs = list(itertools.combinations(applicants.columns, 2))

# 创建一个空的列表来存储结果DataFrame
dfs = []

# 遍历每对申请人，将时间序列和申请人名写入结果 DataFrame
for pair in pairs:
    applicant1, applicant2 = pair
    pair_df = pd.DataFrame({
        '公开（公告）号':a,
        "申请日":time_series,
        "专利类型":b,
        "公开类型":c,
        "知识密集型分类":d,
        "清洁能源产业":e,
        "清洁能源产业":f,
        "被引证次数":g,
        "学科分类":h,
        "新兴产业(主)":i,
        'Source': applicants[applicant1],
        'Target': applicants[applicant2]
    })
    pair_df.dropna(subset=['Target'], inplace=True)  # 只移除'Target'列为空值的行
    dfs.append(pair_df)

# 将所有 DataFrame 拼接成一个
result_df = pd.concat(dfs, ignore_index=True)

print(result_df)

# 在CSV文件中增加end_time列
df = pd.read_csv(result_df, encoding="latin1", dtype=object, low_memory=False)

# 将start_time列转换为日期时间格式
df['start_time'] = pd.to_datetime(df['start_time'], format='%Y-%m-%d')

# 将end_time设置为每年的12月31日
df['end_time'] = df['start_time'].apply(lambda x: x.replace(month=12, day=31))

# 删除未命名的列
df = df.drop(columns=df.columns[df.columns.str.contains('Unnamed')])

# 将end_time列移动到第三列位置
end_time_col = df.pop('end_time')
df.insert(1, 'end_time', end_time_col)

# 保存修改后的数据到CSV文件，使用latin1编码
modified_csv_path = "带时间序列的连边_修改.csv"
df.to_csv(modified_csv_path, index=False, encoding="latin1")

