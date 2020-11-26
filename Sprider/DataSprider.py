from time import sleep

from Sprider import startUrl

from bs4 import BeautifulSoup
import pymysql

from Sprider.Selenium_ini import selenium_

class DataSprider:
    # 单页数据获取
   def Data_Acquisition(resource):
       #装载解析
       soup=BeautifulSoup(resource,'html.parser')
       #内容筛查，获取，获取岗位框所有内容
       div_list=soup.find_all(class_='j_joblist')
       return  div_list[0].find_all(class_='e')
   def  div_bs(div_list):
        # 定义工作名，公司名，薪资,地点要求,待遇，发布时间,公司规模，公司类型
        work_list=[]
        for div in div_list:
            a = div.find(class_='el')
            workname = a.find(class_='jname at')
            time = a.find(class_='time')
            salary = a.find(class_='sal')
            city = a.find(class_='d at')
            try:
                treatment = a.find(class_='tags')['title']
            except:
                treatment=""
            company_div=div.find(class_='er')
            company=company_div.find(class_='cname at')
            company_style = company_div.find(class_='dc at')
            company_size = company_div.find(class_='int at')
            work=[a['href'],workname.string,time.string,company.string,company_style.string,salary.string,city.string,treatment,company_size.string,company['href']]
            work_list.append(work)
        return work_list
   #入库
   def insert(list):
       db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='work',
                            charset='utf8')
       cursor = db.cursor()
       try:
           for i in list:
            print(i[9])
            sql_insert = "Insert into h5 (href,workName,time,company,companySize,salary,city,treatment,companyType,companyHref) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            sleep(3)
            cursor.execute(sql_insert, [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8],i[9]])
           db.commit()
           db.close()
           print("OK")
       except Exception as e:
           print(e)
if __name__ == '__main__':
    da=DataSprider
    se=selenium_(startUrl)
    se.browser_input("HTML5")
    for i in range(1,21):
        resource=se.browser_nextPage(i)
        div=da.Data_Acquisition(resource)
        da.insert(da.div_bs(div))