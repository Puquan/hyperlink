#!/bin/sh
# 此脚本用于第一次创建git仓库并上传
git config --global user.name "puquan"
git config --global user.email "puquan@ualberta.ca"
git config --global credential.helper store
git init 
# 将下行的地址改成你的仓库地址
git remote add origin http://139.217.176.104:31000/Puquan/hyperlink
git add -A 
# 可以在引号内修改你要添加的信息
git commit -m 'test'
git push --set-upstream origin master


####