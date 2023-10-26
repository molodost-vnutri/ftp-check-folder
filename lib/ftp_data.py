import ftplib
from os import mkdir
from os import path
mkdir('Result') if path.exists('Result') == False else ''
def fpt_check(target, port, username, password):
	try:
		port = int(port)
	except:
		return port
	try:
		ftp = ftplib.FTP()
		ftp.connect(target, port, timeout=3)
		ftp.login(username, password)
		ftp.retrlines('LIST')
		with open('Result/ftp_success.txt', 'a+') as file:
			file.write(f'{target}:{port}:{username}:{password}\n')
			print(f'{target}:{port}:{username}:{password} good')
	except ftplib.error_perm as e:
		print(f'Ошибка, недостаточно прав: {e} => {target}:{port}')
	except ftplib.all_errors as e:
		print(f'Произошла ошибка: {e} => {target}:{port}')
