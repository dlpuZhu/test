import imp
from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import time
import pandas as pd
import csv
d = webdriver.Chrome(r'd:\pythonstudy\chromedriver.exe')
d.get('https://www.chinabond.com.cn/cb/cn/xxpl/ywgg/tgywgg/20230129/161991420.shtml')
time.sleep(5)
datas=[]
heads=['序号','债券代码','债券名称','计息方式','债券面额（万元）','年利率(%)']
for i in range(10,92):
   xid = d.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr['+str(i)+']').text.split(' ')[0]# type: ignore
   id = d.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr['+str(i)+']').text.split(" ")[1]
   name = d.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr['+str(i)+']').text.split(" ")[2]
   way = d.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr['+str(i)+']').text.split(" ")[3]
   yuan = d.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr['+str(i)+']').text.split(" ")[4]
   li = d.find_element_by_xpath('/html/body/div[5]/div[2]/div/table/tbody/tr['+str(i)+']').text.split(" ")[5]
   datas.append((xid,id,name,way,yuan,li))

print(datas)
def save(values):#保存函数
    try:
        with open((values+'.csv'),'w',encoding='utf-8',newline='') as fp:   #将数据存入csv文件中
            writer=csv.writer(fp)
            writer.writerow(heads)
            writer.writerows(datas)
        print('数据保存成功')
    except:
        print('数据保存失败')
save('数据')