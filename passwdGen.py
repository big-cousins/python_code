#!/usr/bin/env python

import string
import random
from random import choice

class PasswdGen:
	def __init__(self,app,account,length_of_passwd):
		
		self.app=app
		self.account=account
		self.length_of_passwd=length_of_passwd
		self.length_of_digit=random.randint(1,length_of_passwd-1) #get the random length_of_number
		self.length_of_lowercase=length_of_passwd-self.length_of_digit 
		self.passwd=''

	def passwdGenofNumAndLowercase(self):
		random_lowercase_string=''.join(choice(string.lowercase) for i in range(self.length_of_lowercase))
		random_digit_string=''.join(choice(string.digits) for i in range(self.length_of_digit))
		self.passwd=random_lowercase_string+random_digit_string

			
if __name__=="__main__":
	app=raw_input(">>Please input the app name:")
	account=raw_input(">>Please input the account:")
	length_of_passwd=input(">>please input the length of password(input a number):")
	print "app is %s,account is %s,length_of_passwd is %d" %(app,account,length_of_passwd)
	passwd_gen_object=PasswdGen(app,account,length_of_passwd)
	passwd_gen_object.passwdGenofNumAndLowercase()
	print passwd_gen_object.passwd
	
