# -*- coding: utf-8 -*-

from Excel import readExcel
from Excel import WriteExcel
from File import getAllTypeFiles
from File import getNameFromPath
from File import copyFile


if __name__=='__main__':
    picDir = 'C:\\Users\\HYlqz\\Desktop\\yf员工信息和头像\\员工信息和头像\\新建文件夹\\cropface'
    outDir = 'C:\\Users\\HYlqz\\Desktop\\云浮数据\\照片\\phone\\data\\'
    excelFile = 'C:\\Users\\HYlqz\\Desktop\\云浮数据\\照片\\phone\\data.xls'
    findUsers = []
    
    files = getAllTypeFiles(picDir,'png','jpg')
    users = readExcel(excelFile)
    for file in files:
        name = getNameFromPath(file)
        for user in users:
            subCode = user.getJobnumber()[3:]
            if name == subCode:
                findUsers.append(user)
                #拷贝文件
                copyFile(file,outDir+user.getPhone() + ".jpg")

    for find in findUsers:
        users.remove(find)
    print("未匹配用户个数",len(users))
    findExcel=WriteExcel("C:\\Users\\HYlqz\\Desktop\\云浮数据\\照片\\phone\\unfindExcel.xls",["工号","姓名","部门","电话"])
    findExcel.writeUsersToExcel(users)
    findExcel.save()

    print("匹配的用户个数",len(findUsers))
    findExcel=WriteExcel("C:\\Users\\HYlqz\\Desktop\\云浮数据\\照片\\phone\\findExcel.xls",["工号","姓名","部门","电话"])
    findExcel.writeUsersToExcel(findUsers)
    findExcel.save()

    print("完成。。。")


