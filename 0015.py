#encoding=utf-8
#!/usr/bin/env python
#第 0015 题： 纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

#{
#    "1" : "上海",
#    "2" : "北京",
#    "3" : "成都"
#}
#请将上述内容写到 city.xls 文件中，如下图所示：


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
