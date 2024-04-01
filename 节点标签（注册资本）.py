import pandas as pd
import os

# 读取申请人名单文件
applicant_file = "node_names_with_attributes.xlsx"
df_applicants = pd.read_excel(applicant_file, header=None)

# 读取企业信息文件
company_info_file = "（企查查）大湾区企业基础工商信息.xlsx"
df_company_info = pd.read_excel(company_info_file)

# 遍历申请人名单的每个名字
for index, row in df_applicants.iterrows():
    applicant_name = row[0]
    # 在企业信息文件中查找对应申请人的属性
    attribute = df_company_info[df_company_info["原文件导入名称"] == applicant_name]["注册资本"].values
    if len(attribute) > 0:
        # 如果找到属性，则将其填入申请人名单文件中
        df_applicants.at[index, 3] = attribute[0]

# 保存结果到申请人名单文件
df_applicants.to_excel(applicant_file, index=False, header=False)

