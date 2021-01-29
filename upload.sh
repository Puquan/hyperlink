#!/bin/sh
#此脚本用来上传
git config --global credential.helper store
#根据实际情况修改你的用户名和邮箱
git config --global user.name "puquan"
git config --global user.email "puquan@ualberta.ca"
git add -A
#可以根据需求修改commit信息
git commit -m 'test'
git push origin  
