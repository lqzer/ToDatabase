# -*- coding: utf-8 -*-

import sys
import os
from File import getAllTypeFiles
from File import rename
from Image import convImage

if __name__=='__main__':
   paths = getAllTypeFiles(r"C:\\Users\\HYlqz\Desktop\\yf员工信息和头像\\员工信息和头像\\头像图片\\行政服务中心",".gif")
   for path in paths:
      outpath=rename(path,".gif",".png")
      convImage(path,outpath,"png")

