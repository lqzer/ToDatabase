import xlrd
import xlwt
from User import User


def readExcel(fileName):
    users=[]
    data=xlrd.open_workbook(fileName)
    table=data.sheet_by_index(0)
    nrows=table.nrows
    for rownum in range(1,nrows):
        row=table.row_values(rownum)
        jobNumber=row[0]
        name=row[1]
        department=row[2]
        phone=row[3]
        users.append(User(jobNumber,name,department,phone))
    return users

class WriteExcel:
    """
    写excel, 只能创建xls格式的excel
    param: filename 
    """
    # __fileName=''
    # __workbook=None
    # __worksheet=None
    # __count=0
    
    def __init__(self,fileName,title):
        """
        param: fileName 保存的文件名
        param: excel的列标题头
        """
        self.__fileName=fileName
        self.workbook=xlwt.Workbook(encoding='ascii')
        self.worksheet=self.workbook.add_sheet('sheet1')
        self.count=0
        #title=["工号","姓名","部门","电话"]
        for i in range(0,len(title)):
            self.worksheet.write(self.count,i,title[i])
        self.count += 1

    def writeUserToExcel(self,user):
        self.worksheet.write(self.count,0,user.getJobnumber())
        self.worksheet.write(self.count,1,user.getName())
        self.worksheet.write(self.count,2,user.getDepartment())
        self.worksheet.write(self.count,3,user.getPhone())
        self.count += 1
    
    def writeUsersToExcel(self,users):
        for user in users:
            self.writeUserToExcel(user)

    def save(self):
        self.workbook.save(self.__fileName)
        
if __name__=='__main__':
    # users = readExcel(r"C:\\Users\\HYlqz\\Desktop\\云浮数据\\20200121-员工基本信息.xlsx")
    # print(len(users))
    # for user in users:
    #     print(user.toDict())

    # user = User("03912287","张三","智能方案系统部","18867122190")
    # excel = WriteExcel("./text.xls")
    # excel.writeUserToExcel(user)
    # excel.save()
    
    print("hello")
