import os
import subprocess
import time

def execute_command(command):
    # 执行Shell命令
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # 等待命令执行完毕
    process.wait()

    # 获取命令行输出
    stdout, stderr = process.communicate()

    # 打印命令行输出
    print(stdout.decode("utf-8"))

def run_commands_in_subdirectories(parent_folder, wait_time):
    # 遍历指定文件夹的所有子目录
    for root, dirs, files in os.walk(parent_folder):
        for file in files:
            if file.endswith(".txt"):
                txt_file_path = os.path.join(root, file)

                # 读取txt文件中的命令
                with open(txt_file_path, 'r') as f:
                    commands = f.readlines()

                for command in commands:
                    # 执行命令
                    execute_command(command.strip())

                    # 等待指定时间
                    time.sleep(wait_time)

# 父文件夹路径
parent_folder = "/home/yanbosmu/ts1.5"

# 等待时间（单位：秒）
wait_time = 20
print("one folder tasks finished, begin next task!")

# 执行命令
run_commands_in_subdirectories(parent_folder, wait_time)
