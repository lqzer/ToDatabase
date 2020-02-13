# -*- coding: utf-8 -*-


from PIL import Image
import sys
import os
import base64



def convImage(infile,outfile,format):
    """
    :param infile 输入图片文件路径
    :param outfile 输出图片文件路径
    :param format 转换目标文件格式 jpeg png

    """
    im=Image.open(infile)
    im.convert('RGB')
    im.save(outfile,format)

def compress(inFile,dstFile,scale=2):
    sImg = Image.open(inFile)
    w,h=sImg.size
    dImg=sImg.resize((int(w/scale),int(h/scale)),Image.ANTIALIAS)
    dImg.save(dstFile)

def imageFile2Base64(infile):
    if infile.endswith('png'):
        START="data:image/png;base64,"
    elif infile.endswith('jpg') or infile.endswith('jpeg'):
        START="data:image/jpeg;base64,"
    with open(infile,"rb") as f:
        base64str=base64.b64encode(f.read())
        return START + base64str.decode('ascii')



if __name__== '__main__':
    #convImage("包晓静.gif","foo.png","png")
    
    #basestr = imageFile2Base64("foo.jpg") 
    #print(basestr)

    compress("350.jpg","2244.jpg")
   
       
