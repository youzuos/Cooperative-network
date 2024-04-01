import openpyxl
import networkx as nx

# 读取Excel文件
file_path = "所有数据提取.xlsx"
wb = openpyxl.load_workbook(file_path)
sheet = wb.active

# 创建一个无向图
G = nx.Graph()

# 遍历每一行，构建无向网络
for row in sheet.iter_rows(values_only=True):
    # 过滤空值
    row_values = [value for value in row if value is not None]
    # 添加边
    for i in range(len(row_values)):
        for j in range(i + 1, len(row_values)):
            G.add_edge(row_values[i], row_values[j])

# 将图保存为GraphML文件
graphml_file_path = "graph.graphml"
nx.write_graphml(G, graphml_file_path)