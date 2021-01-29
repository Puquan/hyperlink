import os
from pyperclip import copy
import git
import sys

def init():
    repo_dir = os.getcwd()
    repo_name = repo_dir.split('/')[-1]
    r = git.Repo.init(repo_dir)
    url = input('请输入你git仓库的地址： ')
    #print(url)
    remote = r.create_remote('origin',url=url)
    r.git.add('--all')
    r.git.commit('-m','initialized by init.py')
    r.remote('origin').push('master')
