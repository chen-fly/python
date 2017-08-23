#-*-coding=utf-8-*-

old_file_name = raw_input('请输入复制文件名:')

num = old_file_name.find('.')

name1 = old_file_name[:num]
name2 = old_file_name[num:]

new_file_name = name1+'[复件]'+name2

f = open("../test-python/"+old_file_name, "r")

s = f.read()

f2 = open('../test-python/'+new_file_name, 'w')

f2.write(s)

f.close()
f2.close()

print(s)