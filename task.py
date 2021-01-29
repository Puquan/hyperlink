import os
from pyperclip import copy
import git
import sys
from urllib.parse import unquote
from urllib.parse import quote
from generate import generate_link
from init import init
from upload import upload


def main():
    prompt = int(input('输入模式：\n 1. 将此文件夹新建成git仓库\n 2. 更新git仓库内容\n 3. 生成git仓库notebook链接\n: ' ))
    if prompt==1:
        init()
    elif prompt==2:
        upload()
    elif prompt==3:
        pass
    else:
        print('无法识别指令，关闭程序。')
main()
