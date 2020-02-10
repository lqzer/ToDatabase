# -*- coding: utf-8 -*-

import json

class User:
    __jobNumber = ""
    __name = ""
    __department = ""
    __phone = ""

    def __init__(self,jobNumber,name,department,phone):
        self.__jobNumber = jobNumber
        self.__name=name
        self.__department=department
        self.__phone=phone

    def getJobnumber(self):
        return self.__jobNumber
    def setJobnumber(self,jobnumber):
        self.__jobNumber=jobnumber    
    
    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name=name
    
    def getDepartment(self):
        return self.__department
    def setDepartment(self,department):
        self.__department=department
    
    def getPhone(self):
        return self.__phone
    def setPhone(self,phone):
        self.__phone = phone

    def toDict(self):
        """
        将对象返回为字典
        """
        dict = {}
        dict["jobNumber"]=self.__jobNumber
        dict['department']=self.__department
        dict['name']=self.__name
        dict['phone']=self.__phone
        return dict