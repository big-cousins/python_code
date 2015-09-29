#纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

#{
#   "1":["张三",150,120,100],
#   "2":["李四",90,99,95],
#   "3":["王五",60,66,68]
#}
#请将上述内容写到 student.xls 文件中，如下图所示：
# -*- coding: utf-8 -*-
import xlwt
import simplejson as json



file=xlwt.Workbook()
table=file.add_sheet('students',cell_overwrite_ok=True)
txt=open('e:\python_code\students.txt')

json_txt = json.loads(txt.read().decode('gbk'))

for x in range(len(json_txt)):
        table.write(x,0,x+1)
        y=0
        for record in json_txt[str(x+1)]:
            table.write(x,y+1,record)
            y+=1
file.save('students.xls')
print '写入完毕'
