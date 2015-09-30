#encoding=utf-8
#!/usr/bin/env python

import xlwt
import simplejson as json

txt=open('/home/jeremy/files/python-scripts/python-projects/numbers.txt')        #打开文本
json_txt = json.loads(txt.read())						#读取数据返回列表

file1=xlwt.Workbook()
table=file1.add_sheet('numbers.xls',cell_overwrite_ok=True)

print json_txt

for row in json_txt:								#列表的遍历,用index很方便
	#print json_txt.index(row)
	for col in row:
		table.write(json_txt.index(row),row.index(col),col)
file1.save('numbers.xls')
print '写如完毕' 
