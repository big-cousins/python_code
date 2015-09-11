#有一个目录,放了很多文件(比如.py),统计出每篇日记出现最多的单词
#!/usr/bin/env python

import re
import glob

#得到当前目录下的文件列表
def get_list(files):
	return glob.glob(files)


#返回英文单词列表
def list1(string):
	words=re.findall(r'[A-Za-z]+\b',string)
	return words


#从文件中读取数据
def file_read(filename):
	with open(filename,'r') as fp:
		article=fp.read()
	return article

#计算出出现最多的单词
def most_word_number(word_list):
	str_dict={}
	for item in word_list:
		if item in str_dict:
			str_dict[item]+=1
		else:
			str_dict[item]=1

	str_dict={str_dict[key]:key for key in str_dict}
	return (max(str_dict), str_dict[max(str_dict)])

#主函数,遍历所有文件
def main(path):
	files_list=get_list(path)
	#print files_list
	for name in files_list:
		print name
		word_list=file_read(name)
		words=list1(word_list)
		#print words		
		number,word=most_word_number(words)
		print "The most word is %s ,and %s has %d times" % (word, word, number)

if __name__=='__main__':
	filepath=raw_input(">> ")	
	try:	
		main(filepath)
	except ValueError:
		pass


	
