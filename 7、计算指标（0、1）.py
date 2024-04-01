import numpy as np
import networkx as nx

# 读取节点名称
with open('name.txt', 'r', encoding='utf-8') as f:
    node_names = [line.strip() for line in f]

# 读取邻接矩阵
adj_matrix = np.load('array.npy')

# 创建一个无向图
G = nx.Graph()

# 添加节点
for node_name in node_names:
    G.add_node(node_name)

# 添加边
num_nodes = len(node_names)
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if adj_matrix[i, j] != 0:
            G.add_edge(node_names[i], node_names[j])

# 计算各个指标
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

# 保存指标到文件
with open('centrality_metrics.txt', 'w', encoding='utf-8') as f:
    f.write("Node\tDegree Centrality\tBetweenness Centrality\tCloseness Centrality\tEigenvector Centrality\n")
    for node in node_names:
        f.write(f"{node}\t{degree_centrality.get(node, 0)}\t{betweenness_centrality.get(node, 0)}\t{closeness_centrality.get(node, 0)}\t{eigenvector_centrality.get(node, 0)}\n")

print("Centrality metrics saved to centrality_metrics.txt")
