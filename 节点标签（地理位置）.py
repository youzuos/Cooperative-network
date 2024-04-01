import pandas as pd

# 读取 node_names.csv 文件
node_names_df = pd.read_csv('node_names.csv')

# 读取 node_names_selected.xlsx 文件
attributes_df = pd.read_excel('node_names_selected.xlsx')

# 根据申请人名单遍历，并填入属性
for index, row in node_names_df.iterrows():
    applicant_name = row['名称']
    # 查找申请人对应的属性
    if applicant_name in attributes_df['名称'].values:
        attribute = attributes_df.loc[attributes_df['名称'] == applicant_name, '地理位置'].values[0]
        node_names_df.at[index, '地理位置'] = attribute
    else:
        node_names_df.at[index, '地理位置'] = 'N/A'  # 如果没有找到对应的属性，则填入 N/A

# 将结果保存为一个新的 Excel 文件
node_names_df.to_excel('node_names_with_attributes.xlsx', index=False)
