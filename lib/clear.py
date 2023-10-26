from os import name
from os import system
from lib.menu import menu

def clear():
	system('cls') if name == 'nt' else system('clear')
	menu()
