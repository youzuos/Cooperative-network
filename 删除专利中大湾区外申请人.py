import pandas as pd

# 读取申请人名单
selected_nodes_df = pd.read_excel("node_names_selected.xlsx", header=None)
selected_nodes = set(selected_nodes_df[0])

# 读取所有数据提取0
all_data_df = pd.read_excel("所有数据提取0.xlsx")

# 遍历所有单元格
for row_index, row in all_data_df.iterrows():
    for col_index in range(10, len(all_data_df.columns)):  # 从第10列开始遍历
        node = row[col_index]
        if pd.notna(node) and node not in selected_nodes:
            # 如果该申请人不在申请人名单中，则删除该单元格
            all_data_df.at[row_index, all_data_df.columns[col_index]] = None

# 保存修改后的数据
all_data_df.to_excel("所有数据提取0_updated.xlsx", index=False)
