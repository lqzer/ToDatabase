# -*- coding: utf-8 -*-

import os
import sys
from File import getAllTypeFiles
from Excel import readExcel
from File import getFileNameFromPath
from File import getPath
from File import getNameFromPath
from File import copyFile
from Excel import WriteExcel



if __name__=='__main__':
    #图片文件所在目录
    picDir="C:\\Users\\HYlqz\\Desktop\\yf员工信息和头像\\员工信息和头像\\头像图片\\金山网格"
    picOut="C:\\Users\\HYlqz\\Desktop\\云浮数据\\照片\\all\\data\\"

    findUsers=[]

    paths = getAllTypeFiles(picDir,"png","jpg")
    users = readExcel("C:\\Users\\HYlqz\\Desktop\\云浮数据\\照片\\all\\data.xls")

    print("文件夹里有%d图片文件",len(paths))
    for path in paths:
        name = getNameFromPath(path)
        fileName=getFileNameFromPath(path)
        for user in users:
            if user.getName() in name:
                findUsers.append(user)
                copyFile(path,picOut+fileName)
    
    #往excel里写文件
    print("有%d用户匹配成功",len(findUsers))
    findExcel=WriteExcel("C:\\Users\\HYlqz\\Desktop\\云浮数据\\照片\\all\\findExcel.xls",["工号","姓名","部门","电话"])
    findExcel.writeUsersToExcel(findUsers)
    findExcel.save()

    for user in findUsers:
        users.remove(user)
    #保存未找到的用户
    print("还剩%d用户未匹配成功",len(users))
    findExcel=WriteExcel("C:\\Users\\HYlqz\\Desktop\\云浮数据\\照片\\all\\unfindExcel.xls",["工号","姓名","部门","电话"])
    findExcel.writeUsersToExcel(users)
    findExcel.save()



