'''
Author: sunkr 522697475@qq.com
Date: 2024-03-14 14:11:40
LastEditors: sunkr
LastEditTime: 2024-03-14 14:36:58
Description: file content
'''
import pandas as pd

df = pd.read_excel('所有数据提取0.xlsx')

    # 起始列索引（从0开始）
start_column_index = 10  # 第K列对应的索引

    # 获取每行非空单元格的个数
non_empty_counts = df.iloc[:, start_column_index:].notnull().sum(axis=1)

    # 找到非空单元格数量小于2的行索引
rows_to_delete = non_empty_counts[non_empty_counts < 2].index

    # 删除对应的行
df = df.drop(rows_to_delete, axis=0)

    # 将修改后的 DataFrame 保存到 Excel 文件中
df.to_excel('所有数据提取1.xlsx', index=False)