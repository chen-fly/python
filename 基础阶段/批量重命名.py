#-*-coding=utf-8-*-
import os

#1. ��ȡҪ�������ļ������ļ��е�����
folder_name = input("������Ŀ���ļ���:")

#2. ��ȡҪ���������ļ����е������ļ�����
file_name = os.listdir(folder_name)

#os.chdir(folder_name)

#3. ������
for name in file_name:
    print(name)
    os.rename(name, "����-"+name)