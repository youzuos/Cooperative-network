import networkx as nx
import csv

# 从GraphML文件中读取图
graphml_file_path = "graph.graphml"
G = nx.read_graphml(graphml_file_path)

# 写入节点到 CSV 文件
node_csv_file = "nodes.csv"
with open(node_csv_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Node"])  # 写入表头
    for node in G.nodes:
        writer.writerow([node])

# 写入边到 CSV 文件
edge_csv_file = "edges.csv"
with open(edge_csv_file, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Source", "Target"])  # 写入表头
    for edge in G.edges:
        writer.writerow(edge)
