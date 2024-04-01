'''
Author: sunkr 522697475@qq.com
Date: 2024-03-15 16:38:26
LastEditors: sunkr
LastEditTime: 2024-03-15 17:51:43
Description: file content
'''
import openpyxl
import networkx as nx
import time
import itertools
from tqdm import tqdm
import numpy as np

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

print ()


# 写入矩阵
nodes = list(G.nodes())


num_nodes = len(nodes)

value1 = []

edge_pairs = list(G.edges())
with open("name.txt",'w') as f:
    for i in tqdm(range(len(nodes))):
        f.write(nodes[i]+'\n')

array =  np.zeros((num_nodes,num_nodes))
for i in  tqdm(range(len(edge_pairs))):
    x = nodes.index(edge_pairs[i][0])
    y = nodes.index(edge_pairs[i][1])
    array[x,y] = 1
    array[y,x] = 1

print (array)
np.save('array.npy',array)
print ("end")
