from os import system
def install():
	pip = ['colorama']
	for install in pip:
		system(f'pip install {install}')
