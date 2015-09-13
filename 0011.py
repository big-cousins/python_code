#encoding=utf-8
#敏感词文本文件filter_word.txt,里面的内容为以下内容,当用户输入敏感词语时,则打印出Freedom,否则打印出Human Right.
#!/usr/bin/env python

def read_file(filename):
	l=[]
	with open(filename,'r') as fp:
		for line in fp.readlines():
			l.append(line.strip())
	return l

def input_check(l):
	string=raw_input('Please enter word:')
	if string in l:
		print '注意用词'
	else:
		print string

def main():
	filename='/home/jeremy/files/python-scripts/python-projects/filtered_words.txt'
	l=read_file(filename)
	input_check(l)

if __name__=='__main__':
	main()
