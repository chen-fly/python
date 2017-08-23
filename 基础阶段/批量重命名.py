#-*-coding=utf-8-*-
import os

#1. 获取要重命名文件所在文件夹的名字
folder_name = input("请输入目标文件夹:")

#2. 获取要重命名的文件夹中的所有文件名字
file_name = os.listdir(folder_name)

#os.chdir(folder_name)

#3. 重命名
for name in file_name:
    print(name)
    os.rename(name, "测试-"+name)