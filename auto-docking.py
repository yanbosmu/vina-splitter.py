import os
import subprocess
import time

def rename_folder(folder_path, new_name):
    # 获取文件夹所在的目录和原名称
    dir_path, old_name = os.path.split(folder_path)

    # 构造新路径
    new_path = os.path.join(dir_path, new_name)

    # 重命名文件夹
    os.rename(folder_path, new_path)

def execute_command(command):
    # 执行命令行命令
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 获取命令行输出
    stdout, stderr = process.communicate()

    # 打印命令行输出
    print(stdout.decode("utf-8"))

    # 等待命令行执行完毕
    process.wait()

# 父文件夹路径
parent_folder = "/home/yanbosmu/testfinal"
# 子文件夹列表
subfolders = os.listdir(parent_folder)
# 重命名为"zincnewmo1"的文件夹索引
rename_index = 0

while True:
    # 获取当前要重命名的文件夹路径
    folder_to_rename = os.path.join(parent_folder, subfolders[rename_index])

    # 重命名文件夹为"zincnewmo1"
    rename_folder(folder_to_rename, "zincnewmo1")

    # 执行命令行命令
    command = "./vina --input config.txt"
    execute_command(command)

    # 等待时间
    time.sleep(5400)  # 一个半小时

    # 将之前重命名为"zincnewmo1"的文件夹名称改回原名称
    rename_folder(os.path.join(parent_folder, "zincnewmo1"), subfolders[rename_index])

    # 更新文件夹索引，循环到下一个文件夹
    rename_index = (rename_index + 1) % len(subfolders)
