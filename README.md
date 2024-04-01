# Cooperative-network
Build a network of collaborations with patent data

• Use Python to extract and process patent data to obtain data related to the Greater Bay Area Cooperation Network

• Build a patent applicant cooperation network based on processed data(6563 nodes and 192673 edges)

• visualize the cooperation network with gephi

1.将所有专利提取出分别名为“公开（公告）号”、“申请日”、“专利类型”、“公开类型”、“知识密集型分类”、“清洁能源产业”、“清洁能源产业”、“被引证次数”、“学科分类”、“新兴产业(主)”、“申请人”的列。
2.由于申请人在同一个单元格中且由分号分隔，按分号为间隔符将“申请人”一栏向右分列。
3.将所有个人姓名从申请人名单中删除。
4.将删除个人后申请人名单中仅有一个申请人的专利从专利列表中删除。
5.遍历所有文件夹，将所有提取出的数据拼接到一个文件中。（所有数据提取0.xlsx）
6.按照专利号将信息去重。（所有数据提取0.xlsx）
7.将邻接表另存为一个excel文件(x.xlsx)，生成带权重的无向图，提取图的结点。（name_nodes.csv）
8.使用企查查查询节点的信息(【企查查】批量查询-企业基础工商信息.xlsx)
9.筛选出大湾区的高校、企业、机构(（企查查）大湾区企业基础工商信息.xlsx)
10.筛选出名单中未在企查查中找到的申请人，并手查地址（missing_nodes.xlsx）
11.提取出企查查中查找到的申请人名单及地址，将名单内所有申请人及其地址拼接（node_names_selected.xlsx）
12.从按照专利号将信息去重后的所有专利信息中删除在大湾区以外的所有申请人(所有数据提取0.xlsx)
13.规整邻接表，将空白单元格右侧单元格左移(所有数据提取1.xlsx)
14.删除仅有一个申请人的专利(所有数据提取1.xlsx)
15. 将邻接表另存为一个excel文件(x.xlsx)，生成带权重的无向图，提取图的结点。（name_nodes.csv）；保存图的邻接矩阵（adj_matrix1.csv）
16.遍历第一列的节点名称（name_nodes.csv），并在其右侧单元格填入地理位置。地理位置从“node_names_selected.xlsx”中查找（node_names_with_attributes.xlsx）。
17.根据专利数据（所有数据提取1.xlsx）的邻接矩阵生成边表，并保留边属性（边表.csv）
18.遍历第一列的节点名称（name_nodes.csv），并在其右侧单元格填入类型。类型从“node_names_selected.xlsx”中查找（node_names_with_attributes.xlsx）。
19.遍历第一列的节点名称（name_nodes.csv），并在其右侧单元格填入注册资本。注册资本从“node_names_selected.xlsx”中查找（node_names_with_attributes.xlsx）。
