import os
import shutil

# 定义源文件夹和目标文件夹路径
zinc_folder = "/home/yanbosmu/zinctest3"
target_folder = "/home/yanbosmu/zinctest2"

# 遍历源文件夹中的所有文件和子文件夹
for root, dirs, files in os.walk(zinc_folder):
    for file in files:
        # 构建文件的完整路径
        file_path = os.path.join(root, file)

        # 检查文件内容是否包含"Si"
        with open(file_path, 'r') as f:
            content = f.read()

        if "Si" in content:
            # 构建目标文件的完整路径
            target_file = os.path.join(target_folder, file)

            # 剪切文件到目标文件夹
            shutil.move(file_path, target_file)
            print(f"剪切文件 {file_path} 到 {target_file}")
