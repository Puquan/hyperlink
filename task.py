import os
from pyperclip import copy
import git
import sys
from urllib.parse import unquote
from urllib.parse import quote
from generate import generate_link1
from generate import generate_link2
from init import init
from upload import upload
from generate import search_notebook

def main():
    prompt = int(input('输入模式：\n 1. 将此文件夹新建成git仓库并上传\n 2. 更新git仓库内容\n 3. 生成自己git仓库notebook链接\n 4. 生成他人git仓库notebook链接\n: ' ))
    if prompt==1:
        init()
        print('初始化仓库并上传文件完成')
    elif prompt==2:
        upload()
        print('上传文件已完成')
    elif prompt==3:
        notebook = search_notebook()
        #print(notebook)
        # 如果文件夹中只有一个notebook，自动生成该notebook链接
        if len(notebook)==1:
            link = generate_link(notebook[0])
            print('notebook链接为：')
            print(link)
        elif len(notebook)>1:
            print('检测到多个notebook，请选择一个')
            for index in range(len(notebook)):
                option = index + 1
                print(str(option) + '. ' + str(notebook[index]))
            user_choice = int(input('请输入序号: '))
            link = generate_link1(notebook[user_choice-1])
            print('notebook链接为：')
            print(link)
        elif len(notebook)==0:
            print('未能检测到notebook文件，关闭程序。')
    elif prompt==4:
        git_repo_link = input('请输入该git仓库网址：')
        notebook_path = input('请输入notebook在该仓库的相对地址：')
        link = generate_link2(git_repo_link,notebook_path)
        print(link)
    else:
        print('无法识别指令，关闭程序。')
main()
