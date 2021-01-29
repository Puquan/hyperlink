#!/bin/sh
#此脚本用来恢复到最原先在gitlab上的文本状态
git fetch --all && git reset --hard origin/master && git pull