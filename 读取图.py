import networkx as nx

# 从GraphML文件中读取图
graphml_file_path = "graph.graphml"
G = nx.read_graphml(graphml_file_path)
# 获取节点数量
num_nodes = G.number_of_nodes()
print("节点数量：", num_nodes)

# 获取边的数量
num_edges = G.number_of_edges()
print("边的数量：", num_edges)
