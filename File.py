# -*- coding: utf-8 -*-

import os
import sys
import shutil

def getAllFiles(path):
    """
    获取文件夹下所有文件
    param: path 文件夹
    """
    filepaths=[]
    # os.walk 返回的是一个三元组
    for root, dirnames, files in os.walk(path):
        for file in files:
            filepath=os.path.join(root,file)
            filepaths.append(filepath)
    return filepaths

def getAllTypeFiles(path,type1,type2):
    """
    获取文件夹下所有type类型的文件
    """
    paths = getAllFiles(path)
    paths = [x for x in paths if x.find(type1) != -1 or x.find(type2) != -1]
    return paths

def rename(fileName,oldFormat,newFormat):
    return fileName.replace(oldFormat,newFormat)

def getFileNameFromPath(filePath):
    """
    获取文件名，文件名包含格式
    """
    return filePath[filePath.rfind('\\')+1:]

def getNameFromPath(filePath):
    """
    获取文件名，不包含格式后缀
    """
    return filePath[filePath.rfind('\\')+1:filePath.rfind('.')]

def getPath(filePath):
    return filePath[:filePath.rfind('\\')+1]

def getFileSuffix(filePath):
    return filePath[filePath.rfind('.'):]

def copyFile(src,dst):
    """
    实现文件从src复制到dst
    param：src 源文件
    param: dst 目标文件
    """
    shutil.copy2(src,dst)

if __name__=='__main__':
    paths = getAllFiles('./')
    print(paths)
    paths = getAllTypeFiles('./','py','png')
    print(paths)
    print(rename("/data/log/233.gif",".gif",".png"))

    print(getFileNameFromPath("\\data\\log\\233.gif"))
    print(getPath("\\data\\log\\233.gif"))
    print(getNameFromPath("\\data\\log\\233.gif"))
    print(getFileSuffix("\\data\\log\\233.gif"))