import colorama
import time
from colorama import Fore, Back, init
init()
print(f'{Back.WHITE} {Fore.GREEN} здравствуйте я калкулятор введите 2 числа я их сложу:')
a = input(f'{Fore.GREEN}  первое число - ')
b = input(f'{Fore.GREEN}  второе число - ')
sum = float(a) + float(b)
print(str(a) + '+' + str(b) + '=' + str(sum))