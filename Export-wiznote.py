# coding=utf-8
from __future__ import print_function, unicode_literals
from os import listdir, walk, mkdir, remove, chmod, makedirs
from os.path import isfile, isdir, join, basename, exists
from zipfile import ZipFile
from shutil import rmtree
from stat import S_IWRITE
from time import sleep

# 实现导出md文件夹
wiz_path = 'F:/wiz_save/Data/350341849@qq.com/'
export_path = 'F:/xx/'
tmp_path = 'F:/'
wiz_path_listdir = listdir(wiz_path)

if exists(export_path):
    chmod(export_path, S_IWRITE)
    rmtree(export_path)
    sleep(0.1)
    mkdir(export_path)
else:
    mkdir(export_path)

# 生成目录
for path in walk(wiz_path):

        if path[1] != []:
            for mkdir_path in path[1]:
                new_path = path[0].replace(wiz_path, export_path)
                new_path = join(new_path, mkdir_path)
                makedirs(new_path)
# 生成md文件和文件夹之间的递归


def chuli(new_file_path):
    ziw_path = listdir(new_file_path)
    for ziw in ziw_path:
        new_ziw_path = join(new_file_path, ziw)
        if isfile(new_ziw_path):
            print(new_ziw_path)
            zip_temp = ZipFile(new_ziw_path)
            zip_temp.extract('index.html', tmp_path)
            new_tmp_path = join(tmp_path, 'index.html')
            html = open(new_tmp_path, 'r')
            md = html.read().decode('UTF-16')
            md = md.replace('<!DOCTYPE html><html><head></head><body>', '')
            md = md.replace('</body></html>', '')
            md = md.replace('&nbsp;', ' ')
            md = md.replace('<br/>', '\n')
            new_export_path = new_ziw_path.replace(wiz_path, export_path)
            new_export_path = new_export_path[0:-4]
            print(new_export_path)
            makedown = open(new_export_path, 'w')
            md = md.encode('utf-8')
            makedown.write(md)
            makedown.close()
        else:
            chuli(new_ziw_path)

for file in wiz_path_listdir[2:]:
    file_path = join(wiz_path, file)
    if isdir(file_path):
        new_file_path = join(file_path,)
        if listdir(new_file_path) != []:
            chuli(new_file_path)

print('over')
