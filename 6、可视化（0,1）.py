import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取节点名称
with open('name.txt', 'r') as f:
    node_names = [line.strip() for line in f]

# 读取邻接矩阵
adj_matrix = np.load('array.npy')

# 创建一个无向图
G = nx.Graph()

# 添加节点
for i, node_name in enumerate(node_names):
    G.add_node(node_name)

# 添加边
num_nodes = len(node_names)
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if adj_matrix[i, j] != 0:
            G.add_edge(node_names[i], node_names[j])
print (adj_matrix)

# 绘制图形
pos = nx.spring_layout(G)  # 定义节点的布局
#.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10)  # 绘制图形
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=10, edge_color='gray')
plt.title("Network Visualization")
plt.show()
