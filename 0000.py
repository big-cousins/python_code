#!/usr/bin/env python

from PIL import Image,ImageDraw,ImageFont
import random

def rndChar():
	return random.randint(0,100)
def rndColor():
	return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
	
def addNum(img):
	draw=ImageDraw.Draw(img)
	myfont=ImageFont.truetype('/usr/share/cups/fonts/FreeMonoBold.ttf',36)
	#fillcolor="#ff0000"
	width,height=img.size
	draw.text((2*width/3,0),str(rndChar()),font=myfont,fill=rndColor())
	img.save('result3.jpg')
	return 0

if __name__=='__main__':
	image=Image.open('/home/jeremy/files/test.jpg')
	addNum(image)
