# -*- coding: utf-8 -*-

import os
import sys
from Image import imageFile2Base64
from Excel import readExcel
from File import getAllTypeFiles
from File import getNameFromPath
from User import User
from HttpClient import httpPost
import json


def postData(url,user,picFile):
    body = user.toDict()
    base64 = imageFile2Base64(picFile)
    body["company"]="广东云浮"
    body["base64"]=base64
    response = httpPost(url,body)
    return response


if __name__=='__main__':
    excelFile = "C:\\Users\\HYlqz\\Desktop\\云浮数据\\照片\\all\\summary.xls"
    picDir = "C:\\Users\\HYlqz\\Desktop\\云浮数据\\照片\\all\\data"
    url = "http://localhost:8888/adduser"
    mylog = open('recode.log',mode='a',encoding='utf-8')
    users = readExcel(excelFile)
    picFiles = getAllTypeFiles(picDir,"jpg","png")
    for picFile in picFiles:
        phone=getNameFromPath(picFile)
        for user in users:
            if phone == user.getPhone():
                response = postData(url,user,picFile)
                print(user.toDict(),file=mylog,end=" ")
                print(response.text,file=mylog)
    mylog.close()
    print("导入完成。。。。。")



