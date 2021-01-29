import os
from pyperclip import copy

from urllib.parse import unquote
from urllib.parse import quote
def search_dir_path(git_repo_link):
    index = 0
    for i in range(len(git_repo_link),0,-1):
        if git_repo_link[i-1] == '/':
            index = i-1
            break
    return git_repo_link[index:] + '/'

def generate_link(git_repo_link, notebook_path):

    # hub地址变了请修改这
    jupyterhub_URL = "http://139.217.176.104:30002/"

    # 后缀1
    following1 = 'hub/user-redirect/git-pull?repo='

    # repo地址
    encoded_gitrepo_url = quote(git_repo_link,'utf-8')

    # 后缀2
    following2 = '&urlpath=tree'

    repopath = search_dir_path(git_repo_link)

    # 文件夹地址
    encoded_repopath_url = quote(repopath,'utf-8')

    # notebook地址
    encoded_notebook_url = quote(notebook_path,'utf-8')

    # 后缀3，branch变了修改这
    following3 = '&branch=master'


    url = jupyterhub_URL + following1 + encoded_gitrepo_url + following2 + encoded_repopath_url + encoded_notebook_url + following3

    return url
