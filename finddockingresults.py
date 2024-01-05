import os
import re
import shutil

def search_pdbqt_files(folder_path):
    target_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdbqt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    lines = f.readlines()
                    i = 0
                    while i < len(lines):
                        if "REMARK VINA RESULT:" in lines[i]:
                            result = re.search(r"([-+]?\d*\.\d+|\d+)", lines[i])
                            if result is not None and float(result.group()) < -7.0:
                                target_text = []
                                while i < len(lines):
                                    target_text.append(lines[i].strip())
                                    i += 1
                                target_files.append({
                                    "path": file_path,
                                    "original_name": file,
                                    "text": target_text
                                })
                                break
                        i += 1
    return target_files

def copy_files_to_target_folder(target_files, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    for file_data in target_files:
        source_path = file_data["path"]
        target_path = os.path.join(target_folder, file_data["original_name"])
        shutil.copyfile(source_path, target_path)

def save_txt_file(target_files):
    with open("result1223.txt", "w") as f:
        for file_data in target_files:
            f.write("Original File Path: {}\n".format(file_data["path"]))
            f.write("Original File Name: {}\n".format(file_data["original_name"]))
            f.write("Text:\n")
            for line in file_data["text"]:
                f.write(line + "\n")
            f.write("\n")

# 指定需要搜索的文件夹路径
folder_path = '/home/yanbosmu/zinctesttest'

# 指定目标文件夹的路径
target_folder = '/home/yanbosmu/zinctesttest'

# 执行搜索并记录符合条件的文件信息
target_files = search_pdbqt_files(folder_path)

# 将符合条件的文件复制到目标文件夹中
copy_files_to_target_folder(target_files, target_folder)

# 生成txt文件记录原始文件信息
save_txt_file(target_files)
