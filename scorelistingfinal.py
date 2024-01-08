import os

def process_pdbqt_files(folder_path):
    # 创建一个用于保存结果的新文件
    result_file = open("finalresults.txt", "w")

    # 遍历文件夹中的每个文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # 检查文件是否为pdbqt文件
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)

                # 打开pdbqt文件进行处理
                with open(file_path, "r") as pdbqt_file:
                    lines = pdbqt_file.readlines()

                    for i, line in enumerate(lines):
                        # 检查是否有包含所需文字的行
                        if line.startswith('REMARK VINA RESULT:'):
                            affinity = float(line.split()[3])

                            # 检查第一个数字是否小于-7
                            if affinity < -8:
                                # 将符合条件的行及其下一行写入新文件
                                result_file.write(lines[i-3])
                                result_file.write(lines[i-2])
                                result_file.write(lines[i-1])
                                result_file.write(line)
                                result_file.write(lines[i+1])
                                

    # 关闭新文件
    result_file.close()

process_pdbqt_files("/home/yanbosmu/Bioinfo/Vina-GPU-2.1-main/QuickVina2-GPU-2.1/g")
print("1 folder work finished")

