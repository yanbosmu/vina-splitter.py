import os
import shutil

def move_files_to_folders(source_dir, dest_dir, files_per_folder):
    # 获取文件名列表
    file_names = os.listdir(source_dir)
    num_files = len(file_names)

    # 计算需要创建的目标文件夹数量
    num_folders = num_files // files_per_folder
    if num_files % files_per_folder != 0:
        num_folders += 1

    # 创建目标文件夹
    for i in range(num_folders):
        folder_name = f"{i+1:03d}"
        folder_path = os.path.join(dest_dir, folder_name)
        os.makedirs(folder_path)

    # 移动文件到目标文件夹
    for i, file_name in enumerate(file_names):
        folder_index = i // files_per_folder
        folder_name = f"{folder_index+1:03d}"
        folder_path = os.path.join(dest_dir, folder_name)
        shutil.move(os.path.join(source_dir, file_name), folder_path)

# 源文件夹路径
source_folder = "/home/yanbosmu/zinctest1.1"
# 目标文件夹路径
dest_folder = "/home/yanbosmu/testfinal"

# 每个文件夹包含的文件数量
files_per_folder = 50000

move_files_to_folders(source_folder, dest_folder, files_per_folder)
