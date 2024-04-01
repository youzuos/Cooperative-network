# 打开文本文件进行读取
with open("name.txt", "r", encoding="utf-8") as file:
    # 读取文件内容
    lines = file.readlines()

# 去除每一行开头的空格并保存回列表中
lines_stripped = [line.lstrip() for line in lines]

# 打开文件进行写入（覆盖原文件）
with open("name.txt", "w", encoding="utf-8") as file:
    # 将处理后的内容写入文件
    file.writelines(lines_stripped)
