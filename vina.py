import os
import glob

# 文件夹路径
folder_path = "/home/yanbosmu/test"

# 获取文件夹中的所有文件，仅选择以.pdbqt结尾的文件
file_pattern = os.path.join(folder_path, "*.pdbqt")
files = glob.glob(file_pattern)

# 按每1000个文件的组合分割文件列表
files_groups = [files[i:i+2] for i in range(0, len(files), 1000)]

# 遍历每个文件组合，执行命令
for group in files_groups:
    file_arguments = " ".join("--{}".format(file) for file in group)
    command = "./ {}".format(file_arguments)
    os.system(command)
