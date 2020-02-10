# -*- coding:utf-8 -*-
import requests
import json

def httpPost(url,body):
   #将字符串转为json
   s = json.dumps(body).encode('utf-8')
   r=requests.post(url,data=s,headers={'Content-Type':'application/json;charset=utf-8'})
   return r

def httpGet(url):
   response=requests.get(url)
   return response

if __name__=='__main__':
   url="http://www.baidu.com"
   response=httpGet('http://localhost:8888/hello')
   print(response.content.decode('ascii'))
   dict={}
   dict['name']="tom"
   dict['age']=12
   response=httpPost('http://localhost:8888/adduser',dict)
   print(response.content.decode('ascii'))
   


