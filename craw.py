#encoding=utf-8
#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup 
from urllib2 import urlopen

def get_url(url):
	r=requests.get(url)
	return r.text
count=1	


def main(url):
	
	
	html=get_url(url)
	soup=BeautifulSoup(html)
	elems=soup.find_all('img',{'class':'BDE_Image'})
        #return [elem.get('src')
		#for elem in elems if elem.get('src').find('forum')>-1]
	for elem in elems:
		#print elem
		global count
		file_name=str(count)+'.jpg'
		img_url=elem.get('src')	
		#print img_url
		content=urlopen(img_url).read()
		with open(file_name,'wb') as f:
			f.write(content)
		count+=1
	#print ('\n'.join(img_url))

if __name__=="__main__":
	main('http://tieba.baidu.com/p/2166231880')
