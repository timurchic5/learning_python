from colorama import Fore, Back, Style
import time
whatt = input(Fore.LIGHTMAGENTA_EX + 'Что делаем? +,-,/ или *: ')
a = float(input(Fore.WHITE + 'введите первое число: '))
b = float(input('введите второе число: '))
if whatt == '+':
    c = a + b
    print('результат:' + str(c))
elif whatt == '/' and a == 0 and b == 0:
    print(Fore.RED + 'КОМПЮТЕР ВЗОРВЕТСЯ ЧЕРЕЗ 10')
    time.sleep(1)
    print(Fore.RED + '9')
    time.sleep(1)
    print(Fore.RED + '8')
    time.sleep(1)
    print(Fore.RED + '7')
    time.sleep(1)
    print(Fore.RED + '6')
    time.sleep(1)
    print(Fore.RED + '5')
    time.sleep(1)
    print(Fore.RED + '4')
    time.sleep(1)
    print(Fore.RED + '3')
    time.sleep(1)
    print(Fore.RED + '2')
    time.sleep(1)
    print(Fore.RED + '1')
    time.sleep(1)
    print(Style.RESET_ALL + Back.BLUE + Fore.WHITE + """A problem has been detected and windows has been shut down to prevent damage
to your computer .
The problem seems to be caused by the following file: ntoskrn1.exe
CRITICAL_OBJECT_TERMINATION
If this is the first time you've seen this stop error screen,
restart your computer. If this screen appears again, follow
these steps :
Check to make sure any new hardware or software is properly installed.
If this is a new installation, ask your hardware or software manufacturer
for any Windows updates you might need.
If problems continue, disable or remove any newly installed hardware
or software. Disable BIOS memory options such as caching or shadowing.
If you need to use safe mode to remove or disable components, restart
your computer press F8 to select Advanced Startup Options, and then
select Safe Mode.
Technical Information:
*** STOP: 0x000000f4 (0x00000003, 0x88b45650, 0x88b457c4, 0x805d29ac)
*** ntoskrnl.exe - Address Ox804f9f43 base at 0x804d7000 DateStamp Ox498c114b""")
elif whatt == '-':
    c = a - b
    print('результат:' + str(c))
elif whatt == '/':
    c = a / b
    print('результат:' + str(c))
elif whatt == '*':
    c = a * b
    print('результат:' + str(c))
else:
    print(Fore.CYAN + 'по русски написано +,-,/ или * ты читать не умеешь? иди учись, умник')
time.sleep(1000000)