import requests
from bs4 import BeautifulSoup
import time

def login():
	payload={
		'buttonClicked': 4,
		'err_flag': 0,
		'err_msg': '',
		'info_flag': 0,
		'info_msg': '',
		'redirect_url': '',
		'network_name': 'Guest Network',
		'username': 'azad',
		'password': 'Azad@123'
	}
	res = requests.post('https://1.1.1.1/login.html', data=payload, verify=False)
	html_content = BeautifulSoup(res.text, 'html.parser')
	if(html_content.div.table.tr.td.string=='Login Successful'):
		print('Login Successful')
	else:
		print('Login Failed')

def logout():
	payload={
		'userStatus': 1,
		'err_flag': 0,
		'err_msg': ''
	}
	res = requests.post('https://1.1.1.1/logout.html', data=payload, verify=False)
	if(res.status_code==200):
		print('Logout Successful')
	else:
		print('Logout Failed')

while(True):
	logout()
	login()
	print('Sleeping...')
	time.sleep(1740) #sleep for 29 minutes

