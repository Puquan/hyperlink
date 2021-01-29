import os
from pyperclip import copy
import git
import sys
def upload():
    repo_dir = os.getcwd()
    r = git.Repo(repo_dir)
    r.git.add('--all')
    r.git.commit('-m','upload by upload.py')
    r.remote().push('master')



#reader = r.config_reader()
#a = reader.get_value("user","name")
#b = reader.get_value("user",'password')
