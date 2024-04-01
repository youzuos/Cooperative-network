import pandas as pd

# 读取CSV文件
name_nodes_df = pd.read_csv("node_names.csv")

# 读取Excel文件
excel_df = pd.read_excel("【企查查】批量查询-企业基础工商信息.xlsx")

# 提取CSV文件中的名称列
csv_names = name_nodes_df["名称"]

# 提取Excel文件中的第一列名称
excel_names = excel_df.iloc[:, 0]

# 找出在CSV中出现但在Excel中未出现的名称
missing_names = csv_names[~csv_names.isin(excel_names)]

# 将数组转换为 DataFrame
missing_names_df = pd.DataFrame(missing_names, columns=["名称"])

# 将 DataFrame 写入 Excel 文件
missing_names_df.to_excel("missing_names.xlsx", index=False, engine='openpyxl')
print("已将缺失的名称存入 missing_names.xlsx 文件中。")

