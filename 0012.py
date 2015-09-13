#encoding=utf-8
#!/usr/bin/env python

#导入模块
import re

#从文件中读取信息,以列表的形式返回
def get_list(filename):
	lista=[]
	with open(filename,'r') as fl:
		for line in fl.readlines():
			lista.append(line.strip())
	return lista

#生成对应的正则匹配规则
def gen_pattern(lista):
	pattern=''
	for string in lista:
		pattern+=string+'|'
	return pattern[:-1]  #去掉最后一个'|'

#输入检测后输出
def input_replace(pattern):
	sentence=raw_input("Please input a sentence:")
	print re.sub(pattern,'**',sentence)

#主函数
def main():
	filename='/home/jeremy/files/python-scripts/python-projects/filtered_words.txt'
	lista=get_list(filename)
	pattern=gen_pattern(lista)
	input_replace(pattern)

if __name__=='__main__':
	main()
