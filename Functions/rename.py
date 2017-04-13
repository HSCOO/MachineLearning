import os
def rename_file(file):
    #获取文件列表
    file_list = os.listdir(file)
    # 保存现在的路径
    saved_path = os.getcwd()
    #切换到文件目录
    os.chdir(file)
    for file_name in file_list:
        re_name = file_name.translate(None,'0123456789')
        os.rename(file_name,re_name)
    os.chdir(saved_path)

rename_file('/Users/apple/Downloads/prank')
