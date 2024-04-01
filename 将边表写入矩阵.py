import pandas as pd

# 读取边表.csv文件
df_edges = pd.read_csv("边表.csv")

# 读取节点名称文件
df_node_names = pd.read_excel("node_names.xlsx")

# 创建一个空的邻接矩阵
num_nodes = len(df_node_names)
adj_matrix = pd.DataFrame(0, index=range(num_nodes), columns=range(num_nodes))

# 将节点名称映射到索引
node_name_to_index = {name: index for index, name in enumerate(df_node_names["节点名称"])}

# 根据边表中的信息填充邻接矩阵
for _, row in df_edges.iterrows():
    source_index = node_name_to_index.get(row["Source"])
    target_index = node_name_to_index.get(row["Target"])
    if source_index is not None and target_index is not None:
        adj_matrix.at[source_index, target_index] = row["专利类型"]
        adj_matrix.at[target_index, source_index] = row["专利类型"]  # 因为是无向图，所以同时更新对称位置

# 存储邻接矩阵到CSV文件
adj_matrix.to_csv("专利类型矩阵.csv", index=False, encoding='utf-8-sig')
