#encoding=utf-8
#!/usr/bin/env python

import xlwt
import simplejson as json


txt=open('/home/jeremy/files/python-scripts/python-projects/city.txt')      #读取txt文件
json_txt=json.loads(txt.read())				                    #将文本信息转换为字典


file1=xlwt.Workbook()							    #创建excel文本
table=file1.add_sheet('city',cell_overwrite_ok=True)			    #创建表单


for x in range(len(json_txt)):						    #len(json_txt)为行数
	table.write(x,0,x+1)
	table.write(x,1,json_txt[str(x+1)])
		

file1.save('city.xls')
print "写入完毕"
